"""Teaching content mapped to SVU–KJSCE 2023_1.0, pp. 80–81."""
EXPERIMENTS = [{'unit': '1.1',
  'slug': 'environment',
  'title': 'Django project and development environment',
  'co': 1,
  'module_hours': 7,
  'theory': 'Django is a Python web framework with URL routing, templates, an ORM, forms, '
            'authentication and an administration site. A project contains site configuration; an '
            'app contains a reusable feature. Use a supported Python version and isolate '
            'dependencies in a virtual environment. This repository uses the Django 5.2 LTS '
            'series; requirements.lock records the tested versions.',
  'steps': ['Create and activate a virtual environment with Python 3.13.',
            'Install requirements and inspect pip show Django.',
            'Inspect manage.py, settings.py, urls.py and wsgi.py.',
            'Run migrations, start the development server and open /health/.',
            'Create a separate practice project using startproject; compare its generated '
            'structure.'],
  'code': 'python3.13 -m venv .venv\n'
          'source .venv/bin/activate\n'
          'python -m pip install -r requirements.lock\n'
          'python -m django --version\n'
          'python -m django startproject practice_project\n'
          'python manage.py migrate\n'
          'python manage.py runserver',
  'practical': '/health/',
  'aim': 'Perform and explain django project and development environment using a reproducible '
         'laboratory exercise.',
  'questions': [{'prompt': 'Which file configures installed apps?',
                 'options': ['settings.py', 'views.py', 'manage.txt'],
                 'answer': 0,
                 'correct': 'settings.py'},
                {'prompt': 'Why isolate dependencies?',
                 'options': ['To replace Git',
                             'To serve production traffic',
                             'To avoid conflicting package versions'],
                 'answer': 2,
                 'correct': 'To avoid conflicting package versions'}]},
 {'unit': '1.2',
  'slug': 'javascript',
  'title': 'JavaScript, JSX and verbatim templates',
  'co': 1,
  'module_hours': 7,
  'theory': 'Django renders HTML on the server. React, Vue and other JavaScript libraries can '
            'update selected regions in the browser. JSX is syntax compiled into JavaScript calls; '
            'browsers do not execute raw JSX. Django template delimiters may collide with client '
            'template syntax. The verbatim tag preserves a region literally. This exercise uses a '
            'local small ES module; a separate JSX source and its equivalent compiled calls show '
            'the React boundary without claiming vanilla JavaScript is JSX.',
  'steps': ['Open the template laboratory.',
            'Change the name query parameter and inspect server-rendered output.',
            'Increment the browser counter; reload and observe its reset.',
            'Read the JSX and equivalent React.createElement examples.',
            'Inspect the literal {{ client_value }} output inside a verbatim block.'],
  'code': '{% verbatim %}\n'
          '<p>{{ client_value }}</p>\n'
          '{% endverbatim %}\n'
          '\n'
          '// JSX (compile with a JSX toolchain):\n'
          'const element = <h3>Hello, {name}</h3>;\n'
          '// Equivalent React call:\n'
          'const element = React.createElement("h3", null, "Hello, ", name);',
  'practical': '/course/templates/',
  'aim': 'Perform and explain javascript, jsx and verbatim templates using a reproducible '
         'laboratory exercise.',
  'questions': [{'prompt': 'What happens to JSX before browser execution?',
                 'options': ['Django ORM executes it',
                             'It becomes SQL',
                             'It is compiled to JavaScript'],
                 'answer': 2,
                 'correct': 'It is compiled to JavaScript'},
                {'prompt': 'What does verbatim protect?',
                 'options': ['Database rows', 'Client template delimiters', 'Passwords'],
                 'answer': 1,
                 'correct': 'Client template delimiters'}]},
 {'unit': '1.3',
  'slug': 'git',
  'title': 'Git repositories, remotes, branches and merges',
  'co': 1,
  'module_hours': 7,
  'theory': 'Git stores snapshots in commits and names lines of development with branches. A '
            'remote is a named repository URL; fetch downloads refs and push publishes commits. '
            'GitHub is a hosted Git server. A local bare repository demonstrates the server side '
            'without creating an external account. A production SSH Git server additionally needs '
            'user access control, SSH keys, backups and protected refs. Resolve conflicts in the '
            'working tree before committing the merge.',
  'steps': ['Use the existing Git experiment for branch, merge and conflict practice.',
            'Run the commands below in a disposable directory, not this checkout.',
            'Clone the bare remote into a second working directory.',
            'Create a feature branch, commit a file and push it.',
            'Fetch from the second clone, merge the branch and inspect git log --graph --all.'],
  'code': 'mkdir git-practice && cd git-practice\n'
          'git init --bare classroom.git\n'
          'git clone classroom.git student\n'
          'cd student\n'
          'git switch -c main\n'
          'echo "Lab record" > record.txt\n'
          'git add record.txt\n'
          'git commit -m "Add lab record"\n'
          'git push -u origin main\n'
          'git switch -c feature\n'
          'echo "Observation" >> record.txt\n'
          'git commit -am "Record observation"\n'
          'git switch main\n'
          'git merge feature\n'
          'git push origin main\n'
          'git remote -v',
  'practical': '/',
  'aim': 'Perform and explain git repositories, remotes, branches and merges using a reproducible '
         'laboratory exercise.',
  'questions': [{'prompt': 'Which command downloads remote refs?',
                 'options': ['status', 'fetch', 'init'],
                 'answer': 1,
                 'correct': 'fetch'},
                {'prompt': 'What is a bare repository used for?',
                 'options': ['A shared remote without a working tree',
                             'A CSS theme',
                             'An untracked folder'],
                 'answer': 0,
                 'correct': 'A shared remote without a working tree'}]},
 {'unit': '2.1',
  'slug': 'routing',
  'title': 'URL mapping, function views and class views',
  'co': 2,
  'module_hours': 12,
  'theory': 'A URL pattern maps a request path to a callable. A function-based view receives '
            'HttpRequest and returns HttpResponse. A class-based view uses as_view() to expose a '
            'callable and dispatches HTTP methods to methods such as get(). Named routes let '
            'templates use reverse lookup instead of hardcoded paths. Django templates are escaped '
            'by default; keep user input escaped.',
  'steps': ['Inspect course/urls.py and the experiment function in course/views.py.',
            'Open /course/templates/ to run the TemplateView subclass.',
            'Change ?name=Asha and inspect the response.',
            'Request an unknown experiment slug and confirm HTTP 404.',
            'Compare a function view with TemplateLab.get_context_data.'],
  'code': 'path("templates/", TemplateLab.as_view(), name="templates")\n'
          '\n'
          'class TemplateLab(TemplateView):\n'
          '    template_name = "course/template_lab.html"\n'
          '\n'
          '# Function view:\n'
          'def index(request):\n'
          '    return render(request, "course/index.html", context)',
  'practical': '/course/templates/',
  'aim': 'Perform and explain url mapping, function views and class views using a reproducible '
         'laboratory exercise.',
  'questions': [{'prompt': 'What exposes a CBV as a callable?',
                 'options': ['as_view()', 'objects.all()', 'migrate'],
                 'answer': 0,
                 'correct': 'as_view()'},
                {'prompt': 'What should a view return?',
                 'options': ['A database cursor only', 'A URL pattern', 'HttpResponse'],
                 'answer': 2,
                 'correct': 'HttpResponse'}]},
 {'unit': '2.2',
  'slug': 'templates',
  'title': 'Context variables, loops and template filters',
  'co': 2,
  'module_hours': 12,
  'theory': 'A view supplies a context dictionary to render(). A template reads keys as variables, '
            'loops over collections and applies filters using a pipe. The upper filter changes '
            'presentation, while length counts elements. Template inheritance keeps the header and '
            'navigation consistent. Template rendering is not a place for database writes or '
            'arbitrary Python execution.',
  'steps': ['Open the template laboratory with your name in the query string.',
            'Compare the original name and its uppercase form.',
            'Inspect the three measurements rendered with a for loop.',
            'Enter HTML in the name query parameter and verify it appears as text.',
            'Inspect base.html, extends and block tags.'],
  'code': 'context = {"name": "Asha", "values": [4, 8, 12]}\n'
          'return render(request, "course/template_lab.html", context)\n'
          '\n'
          '{{ name|upper }}\n'
          '{{ values|length }}\n'
          '{% for value in values %}<li>{{ value }}</li>{% endfor %}',
  'practical': '/course/templates/',
  'aim': 'Perform and explain context variables, loops and template filters using a reproducible '
         'laboratory exercise.',
  'questions': [{'prompt': 'Which syntax applies a filter?',
                 'options': ['name.upper()', 'filter(name)', 'name|upper'],
                 'answer': 2,
                 'correct': 'name|upper'},
                {'prompt': 'Why use template inheritance?',
                 'options': ['Replace migrations', 'Reuse the page structure', 'Disable escaping'],
                 'answer': 1,
                 'correct': 'Reuse the page structure'}]},
 {'unit': '2.3',
  'slug': 'static',
  'title': 'Static files, finders and static URLs',
  'co': 2,
  'module_hours': 12,
  'theory': 'Static files include CSS, JavaScript and images. AppDirectoriesFinder searches '
            'installed apps under static/; FileSystemFinder searches STATICFILES_DIRS when '
            'configured. The static template tag constructs a static URL using the configured '
            'storage. findstatic reports where a file is found. collectstatic gathers deployment '
            'assets into STATIC_ROOT. Development runserver serving is not a production static '
            'server.',
  'steps': ['Inspect lab/static/lab/course.css and template static tags.',
            'Run findstatic with verbosity 2 and identify the winning file.',
            'Inspect the default STATICFILES_FINDERS in the Django shell.',
            'Run collectstatic and inspect staticfiles/.',
            'For a FileSystemFinder exercise, add a temporary directory to STATICFILES_DIRS and '
            'repeat findstatic.'],
  'code': 'python manage.py findstatic lab/course.css --verbosity 2\n'
          'python manage.py collectstatic --noinput\n'
          'python manage.py shell -c "from django.conf import settings; '
          'print(settings.STATICFILES_FINDERS)"\n'
          '\n'
          '{% load static %}\n'
          '<link rel="stylesheet" href="{% static \'lab/course.css\' %}">',
  'practical': '/course/templates/',
  'aim': 'Perform and explain static files, finders and static urls using a reproducible '
         'laboratory exercise.',
  'questions': [{'prompt': 'What does collectstatic create?',
                 'options': ['A user account',
                             'A gathered deployment asset directory',
                             'Database migrations'],
                 'answer': 1,
                 'correct': 'A gathered deployment asset directory'},
                {'prompt': 'Which finder searches STATICFILES_DIRS?',
                 'options': ['FileSystemFinder', 'AppConfig', 'URLResolver'],
                 'answer': 0,
                 'correct': 'FileSystemFinder'}]},
 {'unit': '3.1',
  'slug': 'forms',
  'title': 'Forms, validation and cleaned Python values',
  'co': 3,
  'module_hours': 10,
  'theory': 'A bound form contains submitted data. is_valid() runs field conversion, field '
            'validators, clean_field methods and form-wide clean(). cleaned_data contains Python '
            'values such as Decimal rather than raw request strings. Initial values apply to '
            'unbound forms; placeholders are hints, not stored values. POST requests need CSRF '
            'protection and successful writes redirect to prevent duplicate submissions on '
            'refresh.',
  'steps': ['Register and sign in.',
            'Submit a title shorter than three characters and a negative value.',
            'Read both field errors and confirm no row was created.',
            'Submit a valid measurement and refresh after the redirect.',
            'Edit the row and compare the placeholder with its initial value.'],
  'code': 'class ObservationForm(forms.ModelForm):\n'
          '    def clean_value(self):\n'
          '        value = self.cleaned_data["value"]\n'
          '        if value < 0:\n'
          '            raise forms.ValidationError("Use a non-negative value.")\n'
          '        return value\n'
          '\n'
          'if request.method == "POST" and form.is_valid():\n'
          '    observation = form.save(commit=False)',
  'practical': '/course/observations/',
  'aim': 'Perform and explain forms, validation and cleaned python values using a reproducible '
         'laboratory exercise.',
  'questions': [{'prompt': 'When is cleaned_data trustworthy?',
                 'options': ['After successful validation', 'Before binding', 'Only in JavaScript'],
                 'answer': 0,
                 'correct': 'After successful validation'},
                {'prompt': 'Does a placeholder submit a value?',
                 'options': ['Always', 'Only for Decimal', 'No'],
                 'answer': 2,
                 'correct': 'No'}]},
 {'unit': '3.2',
  'slug': 'csv',
  'title': 'CSV processing, graphs and binary responses',
  'co': 3,
  'module_hours': 10,
  'theory': 'Python csv.DictReader maps column headings to row dictionaries. Validate each row '
            'before writing a batch so errors do not leave a partial import. The practical accepts '
            'UTF-8 title,value,notes columns and displays measurements as a server-generated '
            'horizontal graph. Its labels and numeric table remain available without JavaScript. '
            'CSV export uses csv.writer. The self-learning extension streams a real PDF with '
            'FileResponse and ReportLab; binary files require byte buffers, MIME types and '
            'download headers.',
  'steps': ['Download docs/sample-observations.csv from the repository.',
            'Import it while signed in and inspect the graph and table.',
            'Try an invalid negative value; verify the entire batch is rejected.',
            'Download CSV and PDF and inspect their contents.',
            'Compare StringIO for CSV with BytesIO for PDF generation.'],
  'code': 'import csv, io\n'
          'reader = csv.DictReader(io.StringIO(text))\n'
          'for row in reader:\n'
          '    print(row["title"], row["value"])\n'
          '\n'
          '# Binary download:\n'
          'return FileResponse(buffer, as_attachment=True, filename="observations.pdf")',
  'practical': '/course/observations/',
  'aim': 'Perform and explain csv processing, graphs and binary responses using a reproducible '
         'laboratory exercise.',
  'questions': [{'prompt': 'Why validate all rows before bulk_create?',
                 'options': ['Disable UTF-8', 'Make CSV executable', 'Avoid partial imports'],
                 'answer': 2,
                 'correct': 'Avoid partial imports'},
                {'prompt': 'Which buffer stores PDF bytes?',
                 'options': ['QuerySet', 'BytesIO', 'StringIO'],
                 'answer': 1,
                 'correct': 'BytesIO'}]},
 {'unit': '3.3',
  'slug': 'orm',
  'title': 'Models, migrations, CRUD and bulk operations',
  'co': 3,
  'module_hours': 10,
  'theory': 'A model defines database fields and relations. makemigrations creates a versioned '
            'schema change; migrate applies it. The ORM translates query operations to '
            'parameterized SQL. create, filter, update and delete correspond to INSERT, SELECT, '
            'UPDATE and DELETE. bulk_create and bulk_update reduce database round trips but do not '
            'call each object save() or emit its save signals; validate explicitly. Use '
            'transactions for related writes.',
  'steps': ['Run showmigrations and inspect course/migrations/0001_initial.py.',
            'Create, edit and delete your observations in the practical.',
            'Run the ORM commands in a disposable database or with test records.',
            'Inspect a QuerySet.query and compare it with the SQL examples.',
            'Read services.import_csv for the validated bulk_create path and run the notebook '
            'bulk_update exercise.'],
  'code': 'Observation.objects.create(owner=user, title="Latency", value=12)\n'
          'rows = list(Observation.objects.filter(owner=user))\n'
          'for row in rows:\n'
          '    row.notes = "Reviewed"\n'
          'Observation.objects.bulk_update(rows, ["notes"])\n'
          'Observation.objects.filter(owner=user, title="Latency").delete()\n'
          '\n'
          '-- Equivalent CRUD concepts (values should be parameters):\n'
          'INSERT INTO course_observation (owner_id,title,value,notes,created_at) VALUES '
          "(1,'Latency',12,'',CURRENT_TIMESTAMP);\n"
          'SELECT * FROM course_observation WHERE owner_id=1;\n'
          "UPDATE course_observation SET notes='Reviewed' WHERE owner_id=1;\n"
          'DELETE FROM course_observation WHERE owner_id=1;',
  'practical': '/course/observations/',
  'aim': 'Perform and explain models, migrations, crud and bulk operations using a reproducible '
         'laboratory exercise.',
  'questions': [{'prompt': 'What applies schema changes?',
                 'options': ['collectstatic', 'migrate', 'runserver'],
                 'answer': 1,
                 'correct': 'migrate'},
                {'prompt': 'Does bulk_update call each save()?',
                 'options': ['No', 'Yes', 'Only on SQLite'],
                 'answer': 0,
                 'correct': 'No'}]},
 {'unit': '4.1',
  'slug': 'authentication',
  'title': 'Users, sessions, permissions and groups',
  'co': 4,
  'module_hours': 9,
  'theory': 'Authentication identifies a user; authorization determines allowed actions. This '
            'project defines a custom AbstractUser before its first migration and stores '
            'roll_number. Django hashes passwords, rotates session credentials at login, and '
            'supports password change and token-based reset. The development email backend prints '
            'reset messages to the server console. Each observation belongs to its creator. The '
            'instructor export requires an explicit permission; staff access and model permissions '
            'are separate concepts.',
  'steps': ['Register two users and create an observation for each.',
            'Verify each account sees only its own rows.',
            'Change a password, then request a password reset using your registered email.',
            'Follow the reset URL printed by the console backend; a token is single-use.',
            'Create an Instructors group in admin, assign export_observation and test '
            '/course/instructor/export/ with and without it.',
            'Use the POST logout button and verify protected routes redirect to login.'],
  'code': 'from django.contrib.auth.models import Group, Permission\n'
          'group, _ = Group.objects.get_or_create(name="Instructors")\n'
          'permission = Permission.objects.get(codename="export_observation", '
          'content_type__app_label="course")\n'
          'group.permissions.add(permission)\n'
          'user.groups.add(group)\n'
          'user.has_perm("course.export_observation")',
  'practical': '/course/register/',
  'aim': 'Perform and explain users, sessions, permissions and groups using a reproducible '
         'laboratory exercise.',
  'questions': [{'prompt': 'How do authentication and authorization differ?',
                 'options': ['Identity versus allowed actions',
                             'They are identical',
                             'Authorization hashes passwords'],
                 'answer': 0,
                 'correct': 'Identity versus allowed actions'},
                {'prompt': 'Where do reset emails go in local development?',
                 'options': ['Automatically to Gmail', 'Git commits', 'Server console'],
                 'answer': 2,
                 'correct': 'Server console'}]},
 {'unit': '4.2',
  'slug': 'admin',
  'title': 'Django administration, filters and actions',
  'co': 4,
  'module_hours': 9,
  'theory': 'Django admin is a trusted staff interface generated from model metadata. Registering '
            'a ModelAdmin controls list columns, search fields, filters and actions. This lab '
            'customizes the site headings and user fieldsets, adds owner/date filters and a '
            'clear-notes action. Staff users still need model permissions. Admin actions can '
            'change many records: inspect the selection before confirming an operation.',
  'steps': ['Create a superuser from the terminal; never commit credentials.',
            'Open /admin/ and inspect Users, Groups and Observations.',
            'Search observations by title or username and filter by owner.',
            'Select test observations and run Clear notes.',
            'Create a staff account with view-only permissions and compare its controls.'],
  'code': 'python manage.py createsuperuser\n'
          '\n'
          '@admin.register(Observation)\n'
          'class ObservationAdmin(admin.ModelAdmin):\n'
          '    list_display = ("title", "owner", "value", "created_at")\n'
          '    list_filter = ("created_at", "owner")\n'
          '    search_fields = ("title", "owner__username")',
  'practical': '/admin/',
  'aim': 'Perform and explain django administration, filters and actions using a reproducible '
         'laboratory exercise.',
  'questions': [{'prompt': 'Does is_staff grant every model permission?',
                 'options': ['Yes', 'Only for custom users', 'No'],
                 'answer': 2,
                 'correct': 'No'},
                {'prompt': 'Which option creates sidebar filters?',
                 'options': ['STATIC_ROOT', 'list_filter', 'list_display'],
                 'answer': 1,
                 'correct': 'list_filter'}]},
 {'unit': '5.1',
  'slug': 'fastapi',
  'title': 'REST endpoints and Pydantic validation',
  'co': 5,
  'module_hours': 7,
  'theory': 'REST uses resource URLs and HTTP semantics: GET reads, POST creates (201), PUT '
            'replaces, DELETE removes (204), and missing resources return 404. JSON is a '
            'representation format. FastAPI builds on ASGI with type-driven validation and OpenAPI '
            'documentation. It supports async functions for awaitable I/O; async alone does not '
            'accelerate CPU work or blocking database calls. Django REST Framework integrates '
            'closely with Django ORM/auth/admin; FastAPI suits a separate typed API. Neither is '
            'universally superior. The companion API uses SQLite persistence and Pydantic '
            'constraints, not a process-local dictionary.',
  'steps': ['Start the separate FastAPI service on port 8001.',
            'Open /docs and inspect the generated schemas.',
            'POST an observation, then GET it by its returned integer ID.',
            'Filter the collection with the min_value query parameter.',
            'Try a short title or negative value and inspect HTTP 422.',
            'Replace and delete the resource; verify a subsequent GET returns 404.'],
  'code': 'uvicorn api.main:app --port 8001\n'
          '\n'
          'curl -X POST http://127.0.0.1:8001/observations -H "Content-Type: application/json" -d '
          '\'{"title":"Latency","value":12}\'\n'
          'curl "http://127.0.0.1:8001/observations?min_value=10"',
  'practical': 'http://127.0.0.1:8001/docs',
  'aim': 'Perform and explain rest endpoints and pydantic validation using a reproducible '
         'laboratory exercise.',
  'questions': [{'prompt': 'Which status signals schema validation failure?',
                 'options': ['204', '422', '201'],
                 'answer': 1,
                 'correct': '422'},
                {'prompt': 'What does async help with?',
                 'options': ['Awaitable I/O concurrency',
                             'Every CPU computation',
                             'Replacing authentication'],
                 'answer': 0,
                 'correct': 'Awaitable I/O concurrency'}]},
 {'unit': '5.2',
  'slug': 'testing',
  'title': 'Endpoint tests and deployment',
  'co': 5,
  'module_hours': 7,
  'theory': 'Tests should assert status codes, response fields, persistence and error cases. '
            'FastAPI TestClient runs the ASGI app without a network server. This repository uses '
            'an isolated temporary SQLite database per test. Django tests check validation, '
            'ownership, permissions, CSV atomicity, authentication and rendered pages. Deployment '
            'needs a production server, private database volume, secret configuration, HTTPS and '
            'static serving. The supplied container and guide are a reproducible starting point; a '
            'successful local run does not prove a hosted deployment.',
  'steps': ['Run the Django tests and FastAPI pytest suite.',
            'Read tests for 201 creation, 422 validation and 404 missing records.',
            'Run check, migration drift check and collectstatic.',
            'Build the Docker image and run Django using the documented environment variables.',
            'Follow docs/deployment.md for HTTPS, static serving, volumes and a release '
            'checklist.'],
  'code': 'python manage.py test\n'
          'python -m pytest api/tests.py -q\n'
          'python manage.py check\n'
          'python manage.py makemigrations --check --dry-run\n'
          'python manage.py collectstatic --noinput\n'
          'docker build -t django-vlab .',
  'practical': '/course/',
  'aim': 'Perform and explain endpoint tests and deployment using a reproducible laboratory '
         'exercise.',
  'questions': [{'prompt': 'What should an endpoint test verify?',
                 'options': ['Status and response data',
                             'Only that no exception occurred',
                             'Only file names'],
                 'answer': 0,
                 'correct': 'Status and response data'},
                {'prompt': 'Why isolate the test database?',
                 'options': ['Disable validation',
                             'Increase API permissions',
                             'Prevent tests altering real observations'],
                 'answer': 2,
                 'correct': 'Prevent tests altering real observations'}]}]
