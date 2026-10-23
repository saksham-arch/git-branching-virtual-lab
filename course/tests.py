import io
from django.contrib.auth.models import Group, Permission
from django.core import mail
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client, override_settings
from django.urls import reverse
from .models import User, Observation

class CourseTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('student', 'student@example.com', 'StrongPassword!789')
        self.other = User.objects.create_user('other', password='StrongPassword!789')

    def test_original_experiment_and_legacy_course_redirect(self):
        self.assertRedirects(self.client.get('/course/'), '/')
        response = self.client.get('/')
        self.assertContains(response, 'Git Branching, Merging and Conflict Resolution')
        self.assertNotContains(response, 'SVU')
        self.assertNotContains(response, 'List of experiments')

    def test_git_prediction_and_verbatim(self):
        response = self.client.get('/course/react/')
        self.assertContains(response, 'Predict the merge')
        self.assertContains(response, '{{ branch_name }}')

    def test_save_git_quiz_attempt(self):
        self.client.force_login(self.user)
        response = self.client.post('/course/attempts/save/', {'title':'Git quiz — main', 'value':75, 'notes':'3/4'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Observation.objects.get().owner, self.user)
        self.assertEqual(self.client.post('/course/attempts/save/', {'title':'Git quiz', 'value':101}).status_code, 400)

    def test_crud_validation_and_ownership(self):
        self.client.force_login(self.user)
        self.client.post('/course/observations/', {'title': 'x', 'value': '-1'})
        self.assertEqual(Observation.objects.count(), 0)
        self.client.post('/course/observations/', {'title': 'Latency', 'value': '12.5', 'notes': 'First'})
        row = Observation.objects.get()
        self.assertEqual(row.owner, self.user)
        self.client.post(f'/course/observations/?edit={row.pk}', {'title': 'Revised', 'value': '13'})
        row.refresh_from_db()
        self.assertEqual(row.title, 'Revised')
        self.client.force_login(self.other)
        self.assertNotContains(self.client.get('/course/observations/'), 'Revised')
        self.assertEqual(self.client.get(f'/course/observations/?edit={row.pk}').status_code, 404)
        self.assertEqual(self.client.post(f'/course/observations/{row.pk}/delete/').status_code, 404)
        self.client.force_login(self.user)
        self.assertEqual(self.client.get(f'/course/observations/{row.pk}/delete/').status_code, 200)
        self.assertTrue(Observation.objects.exists())
        self.client.post(f'/course/observations/{row.pk}/delete/')
        self.assertFalse(Observation.objects.exists())

    def test_csv_atomic_import_and_exports(self):
        self.client.force_login(self.user)
        def upload(text):
            return self.client.post('/course/csv/import/', {'file': SimpleUploadedFile('data.csv', text.encode())})
        upload('title,value,notes\nValid,4,one\nInvalid,-1,two\n')
        self.assertEqual(Observation.objects.count(), 0)
        response = upload('title,value,notes\nLatency,4,one\nThroughput,8,two\n')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Observation.objects.count(), 2)
        self.assertContains(self.client.get('/course/observations/'), 'Quiz score history')
        self.assertContains(self.client.get('/course/csv/export/'), 'Latency,4.00,one', status_code=200)
        pdf = self.client.get('/course/pdf/')
        self.assertEqual(pdf['Content-Type'], 'application/pdf')
        self.assertTrue(b''.join(pdf.streaming_content).startswith(b'%PDF'))
        upload('wrong,columns\nA,B\n')
        self.assertEqual(Observation.objects.count(), 2)

    def test_csv_formula_protection(self):
        self.client.force_login(self.user)
        Observation.objects.create(owner=self.user, title='=SUM(A1)', value=2)
        self.assertContains(self.client.get('/course/csv/export/'), "'=SUM(A1)")

    def test_permissions_groups_and_admin(self):
        self.client.force_login(self.user)
        self.assertEqual(self.client.get('/course/instructor/export/').status_code, 403)
        group = Group.objects.create(name='Instructors')
        group.permissions.add(Permission.objects.get(codename='export_observation'))
        self.user.groups.add(group)
        self.assertEqual(self.client.get('/course/instructor/export/').status_code, 200)
        self.assertEqual(self.client.get('/admin/').status_code, 302)
        admin = User.objects.create_superuser('teacher', 'teacher@example.com', 'StrongPassword!789')
        self.client.force_login(admin)
        self.assertContains(self.client.get('/admin/'), 'Git Laboratory Administration')
        self.assertEqual(self.client.get('/admin/course/observation/').status_code, 200)

    @override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
    def test_registration_login_password_reset_and_logout(self):
        response = self.client.post('/course/register/', {'username': 'newstudent', 'email': 'new@example.com', 'roll_number': '121', 'password1': 'MyStrongLabPass!789', 'password2': 'MyStrongLabPass!789'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newstudent').exists())
        self.client.post('/accounts/logout/')
        self.assertEqual(self.client.get('/course/observations/').status_code, 302)
        self.assertTrue(self.client.login(username='student', password='StrongPassword!789'))
        self.assertEqual(self.client.post('/accounts/password_change/', {'old_password': 'StrongPassword!789', 'new_password1': 'ChangedLabPassword!123', 'new_password2': 'ChangedLabPassword!123'}).status_code, 302)
        self.client.post('/accounts/logout/')
        self.client.post('/accounts/password_reset/', {'email': 'student@example.com'})
        self.assertEqual(len(mail.outbox), 1)
        import re
        url = re.search(r'http://testserver([^\s]+)', mail.outbox[0].body).group(1)
        response = self.client.get(url)
        reset_url = response.url
        response = self.client.post(reset_url, {'new_password1': 'ResetLabPassword!123', 'new_password2': 'ResetLabPassword!123'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.client.login(username='student', password='ResetLabPassword!123'))
        self.assertContains(self.client.get(url, follow=True), 'invalid or has expired')

    def test_csrf_required_and_logout_is_post_only(self):
        client = Client(enforce_csrf_checks=True)
        client.force_login(self.user)
        self.assertEqual(client.post('/course/observations/', {'title': 'Valid', 'value': 1}).status_code, 403)
        self.assertEqual(client.get('/accounts/logout/').status_code, 405)
