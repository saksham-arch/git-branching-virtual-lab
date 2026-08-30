from django.test import TestCase
from django.urls import reverse

class ExperimentTests(TestCase):
    def test_experiment_page_renders_client_app(self):
        response = self.client.get(reverse("lab:experiment"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Git Branching, Merging and Conflict Resolution")
        self.assertContains(response, "lab/app.js")

    def test_experiment_api_describes_lab(self):
        response = self.client.get(reverse("lab:experiment-api"))
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload["delivery"], "Django + client-side interactive laboratory")
        self.assertGreaterEqual(payload["section_count"], 16)

    def test_health_endpoint_identifies_django(self):
        response = self.client.get(reverse("lab:health"))
        self.assertEqual(response.json(), {"status": "ok", "framework": "Django"})
