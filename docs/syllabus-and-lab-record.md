# Syllabus coverage and laboratory record

Reference: **SVU–KJSCE 2023_1.0 TY B Tech COMP BoS, pages 80–81**, transcribed from the supplied syllabus. The module hour totals are 7 + 12 + 10 + 9 + 7 = **45 hours**. Hours belong to modules, not individual experiments. CO numbers below follow the supplied mapping; no official CO wording was supplied.

| Unit | Experiment | CO | Working evidence / source |
|---|---|---|---|
| 1.1 | [Django project and development environment](../course/catalog.py) | CO1 | manage.py, gitlab_project/settings.py, requirements.lock; /health/ |
| 1.2 | [JavaScript, JSX and verbatim templates](../course/catalog.py) | CO1 | /course/templates/, /course/react/; frontend/src/main.jsx; verbatim template |
| 1.3 | [Git repositories, remotes, branches and merges](../course/catalog.py) | CO1 | Original / Git experiment; bare-server and remote commands in unit procedure |
| 2.1 | [URL mapping, function views and class views](../course/catalog.py) | CO2 | course/urls.py; experiment FBV and TemplateLab CBV |
| 2.2 | [Context variables, loops and template filters](../course/catalog.py) | CO2 | course/templates/course/template_lab.html; context, loop, upper, length |
| 2.3 | [Static files, finders and static URLs](../course/catalog.py) | CO2 | lab/static/; findstatic and collectstatic commands |
| 3.1 | [Forms, validation and cleaned Python values](../course/catalog.py) | CO3 | course/forms.py; validated, persisted /course/observations/ |
| 3.2 | [CSV processing, graphs and binary responses](../course/catalog.py) | CO3 | course/services.py; CSV import/export, graph, PDF download |
| 3.3 | [Models, migrations, CRUD and bulk operations](../course/catalog.py) | CO3 | course/models.py; initial migration; CRUD views; import bulk_create; notebook bulk_update and SQL |
| 4.1 | [Users, sessions, permissions and groups](../course/catalog.py) | CO4 | Custom User; registration; Django auth routes; owner filters; group permission test |
| 4.2 | [Django administration, filters and actions](../course/catalog.py) | CO4 | course/admin.py; site headings, UserAdmin fields, list filters, search and action |
| 5.1 | [REST endpoints and Pydantic validation](../course/catalog.py) | CO5 | api/main.py; persistent CRUD, path/query parameters, Pydantic, /docs |
| 5.2 | [Endpoint tests and deployment](../course/catalog.py) | CO5 | course/tests.py, lab/tests.py, api/tests.py; Dockerfile and deployment guide |

Unit 1.3 also includes a [two-clone, hosted GitHub and SSH server practical](git-server-practical.md).

## Experiment records
Use the following record structure for each unit. Enter your own observed results; expected behavior is not a claim that a student performed an experiment.

Student name: __________  Roll number: __________  Batch: __________  Date: __________

## 1.1 — Django project and development environment

**Aim:** Perform and explain django project and development environment using a reproducible laboratory exercise.

**Outcome:** CO1

### Theory
Django is a Python web framework with URL routing, templates, an ORM, forms, authentication and an administration site. A project contains site configuration; an app contains a reusable feature. Use a supported Python version and isolate dependencies in a virtual environment. This repository uses the Django 5.2 LTS series; requirements.lock records the tested versions.

### Procedure
1. Create and activate a virtual environment with Python 3.13.
2. Install requirements and inspect pip show Django.
3. Inspect manage.py, settings.py, urls.py and wsgi.py.
4. Run migrations, start the development server and open /health/.
5. Create a separate practice project using startproject; compare its generated structure.

### Source / commands
```text
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.lock
python -m django --version
python -m django startproject practice_project
python manage.py migrate
python manage.py runserver
```

**Practical route:** `/health/`

**Observation record:** Input / command: __________; result / status: __________; invalid-input result: __________; screenshot reference: __________.

**Result:** Explain what your output demonstrates: __________.

### Viva / post-lab questions
- Which file configures installed apps? Answer: settings.py
- Why isolate dependencies? Answer: To avoid conflicting package versions

## 1.2 — JavaScript, JSX and verbatim templates

**Aim:** Perform and explain javascript, jsx and verbatim templates using a reproducible laboratory exercise.

**Outcome:** CO1

### Theory
Django renders HTML on the server. React, Vue and other JavaScript libraries can update selected regions in the browser. JSX is syntax compiled into JavaScript calls; browsers do not execute raw JSX. Django template delimiters may collide with client template syntax. The verbatim tag preserves a region literally. This exercise uses a local small ES module; a separate JSX source and its equivalent compiled calls show the React boundary without claiming vanilla JavaScript is JSX.

### Procedure
1. Open the template laboratory.
2. Change the name query parameter and inspect server-rendered output.
3. Increment the browser counter; reload and observe its reset.
4. Read the JSX and equivalent React.createElement examples.
5. Inspect the literal {{ client_value }} output inside a verbatim block.

### Source / commands
```text
{% verbatim %}
<p>{{ client_value }}</p>
{% endverbatim %}

// JSX (compile with a JSX toolchain):
const element = <h3>Hello, {name}</h3>;
// Equivalent React call:
const element = React.createElement("h3", null, "Hello, ", name);
```

**Practical route:** `/course/templates/`

**Observation record:** Input / command: __________; result / status: __________; invalid-input result: __________; screenshot reference: __________.

**Result:** Explain what your output demonstrates: __________.

### Viva / post-lab questions
- What happens to JSX before browser execution? Answer: It is compiled to JavaScript
- What does verbatim protect? Answer: Client template delimiters

## 1.3 — Git repositories, remotes, branches and merges

**Aim:** Perform and explain git repositories, remotes, branches and merges using a reproducible laboratory exercise.

**Outcome:** CO1

### Theory
Git stores snapshots in commits and names lines of development with branches. A remote is a named repository URL; fetch downloads refs and push publishes commits. GitHub is a hosted Git server. A local bare repository demonstrates the server side without creating an external account. A production SSH Git server additionally needs user access control, SSH keys, backups and protected refs. Resolve conflicts in the working tree before committing the merge.

### Procedure
1. Use the existing Git experiment for branch, merge and conflict practice.
2. Run the commands below in a disposable directory, not this checkout.
3. Clone the bare remote into a second working directory.
4. Create a feature branch, commit a file and push it.
5. Fetch from the second clone, merge the branch and inspect git log --graph --all.

### Source / commands
```text
mkdir git-practice && cd git-practice
git init --bare classroom.git
git clone classroom.git student
cd student
git switch -c main
echo "Lab record" > record.txt
git add record.txt
git commit -m "Add lab record"
git push -u origin main
git switch -c feature
echo "Observation" >> record.txt
git commit -am "Record observation"
git switch main
git merge feature
git push origin main
git remote -v
```

**Practical route:** `/`

**Observation record:** Input / command: __________; result / status: __________; invalid-input result: __________; screenshot reference: __________.

**Result:** Explain what your output demonstrates: __________.

### Viva / post-lab questions
- Which command downloads remote refs? Answer: fetch
- What is a bare repository used for? Answer: A shared remote without a working tree

## 2.1 — URL mapping, function views and class views

**Aim:** Perform and explain url mapping, function views and class views using a reproducible laboratory exercise.

**Outcome:** CO2

### Theory
A URL pattern maps a request path to a callable. A function-based view receives HttpRequest and returns HttpResponse. A class-based view uses as_view() to expose a callable and dispatches HTTP methods to methods such as get(). Named routes let templates use reverse lookup instead of hardcoded paths. Django templates are escaped by default; keep user input escaped.

### Procedure
1. Inspect course/urls.py and the experiment function in course/views.py.
2. Open /course/templates/ to run the TemplateView subclass.
3. Change ?name=Asha and inspect the response.
4. Request an unknown experiment slug and confirm HTTP 404.
5. Compare a function view with TemplateLab.get_context_data.

### Source / commands
```text
path("templates/", TemplateLab.as_view(), name="templates")

class TemplateLab(TemplateView):
    template_name = "course/template_lab.html"

# Function view:
def index(request):
    return render(request, "course/index.html", context)
```

**Practical route:** `/course/templates/`

**Observation record:** Input / command: __________; result / status: __________; invalid-input result: __________; screenshot reference: __________.

**Result:** Explain what your output demonstrates: __________.

### Viva / post-lab questions
- What exposes a CBV as a callable? Answer: as_view()
- What should a view return? Answer: HttpResponse

## 2.2 — Context variables, loops and template filters

**Aim:** Perform and explain context variables, loops and template filters using a reproducible laboratory exercise.

**Outcome:** CO2

### Theory
A view supplies a context dictionary to render(). A template reads keys as variables, loops over collections and applies filters using a pipe. The upper filter changes presentation, while length counts elements. Template inheritance keeps the header and navigation consistent. Template rendering is not a place for database writes or arbitrary Python execution.

### Procedure
1. Open the template laboratory with your name in the query string.
2. Compare the original name and its uppercase form.
3. Inspect the three measurements rendered with a for loop.
4. Enter HTML in the name query parameter and verify it appears as text.
5. Inspect base.html, extends and block tags.

### Source / commands
```text
context = {"name": "Asha", "values": [4, 8, 12]}
return render(request, "course/template_lab.html", context)

{{ name|upper }}
{{ values|length }}
{% for value in values %}<li>{{ value }}</li>{% endfor %}
```

**Practical route:** `/course/templates/`

**Observation record:** Input / command: __________; result / status: __________; invalid-input result: __________; screenshot reference: __________.

**Result:** Explain what your output demonstrates: __________.

### Viva / post-lab questions
- Which syntax applies a filter? Answer: name|upper
- Why use template inheritance? Answer: Reuse the page structure

## 2.3 — Static files, finders and static URLs

**Aim:** Perform and explain static files, finders and static urls using a reproducible laboratory exercise.

**Outcome:** CO2

### Theory
Static files include CSS, JavaScript and images. AppDirectoriesFinder searches installed apps under static/; FileSystemFinder searches STATICFILES_DIRS when configured. The static template tag constructs a static URL using the configured storage. findstatic reports where a file is found. collectstatic gathers deployment assets into STATIC_ROOT. Development runserver serving is not a production static server.

### Procedure
1. Inspect lab/static/lab/course.css and template static tags.
2. Run findstatic with verbosity 2 and identify the winning file.
3. Inspect the default STATICFILES_FINDERS in the Django shell.
4. Run collectstatic and inspect staticfiles/.
5. For a FileSystemFinder exercise, add a temporary directory to STATICFILES_DIRS and repeat findstatic.

### Source / commands
```text
python manage.py findstatic lab/course.css --verbosity 2
python manage.py collectstatic --noinput
python manage.py shell -c "from django.conf import settings; print(settings.STATICFILES_FINDERS)"

{% load static %}
<link rel="stylesheet" href="{% static 'lab/course.css' %}">
```

**Practical route:** `/course/templates/`

**Observation record:** Input / command: __________; result / status: __________; invalid-input result: __________; screenshot reference: __________.

**Result:** Explain what your output demonstrates: __________.

### Viva / post-lab questions
- What does collectstatic create? Answer: A gathered deployment asset directory
- Which finder searches STATICFILES_DIRS? Answer: FileSystemFinder

## 3.1 — Forms, validation and cleaned Python values

**Aim:** Perform and explain forms, validation and cleaned python values using a reproducible laboratory exercise.

**Outcome:** CO3

### Theory
A bound form contains submitted data. is_valid() runs field conversion, field validators, clean_field methods and form-wide clean(). cleaned_data contains Python values such as Decimal rather than raw request strings. Initial values apply to unbound forms; placeholders are hints, not stored values. POST requests need CSRF protection and successful writes redirect to prevent duplicate submissions on refresh.

### Procedure
1. Register and sign in.
2. Submit a title shorter than three characters and a negative value.
3. Read both field errors and confirm no row was created.
4. Submit a valid measurement and refresh after the redirect.
5. Edit the row and compare the placeholder with its initial value.

### Source / commands
```text
class ObservationForm(forms.ModelForm):
    def clean_value(self):
        value = self.cleaned_data["value"]
        if value < 0:
            raise forms.ValidationError("Use a non-negative value.")
        return value

if request.method == "POST" and form.is_valid():
    observation = form.save(commit=False)
```

**Practical route:** `/course/observations/`

**Observation record:** Input / command: __________; result / status: __________; invalid-input result: __________; screenshot reference: __________.

**Result:** Explain what your output demonstrates: __________.

### Viva / post-lab questions
- When is cleaned_data trustworthy? Answer: After successful validation
- Does a placeholder submit a value? Answer: No

## 3.2 — CSV processing, graphs and binary responses

**Aim:** Perform and explain csv processing, graphs and binary responses using a reproducible laboratory exercise.

**Outcome:** CO3

### Theory
Python csv.DictReader maps column headings to row dictionaries. Validate each row before writing a batch so errors do not leave a partial import. The practical accepts UTF-8 title,value,notes columns and displays measurements as a server-generated horizontal graph. Its labels and numeric table remain available without JavaScript. CSV export uses csv.writer. The self-learning extension streams a real PDF with FileResponse and ReportLab; binary files require byte buffers, MIME types and download headers.

### Procedure
1. Download docs/sample-observations.csv from the repository.
2. Import it while signed in and inspect the graph and table.
3. Try an invalid negative value; verify the entire batch is rejected.
4. Download CSV and PDF and inspect their contents.
5. Compare StringIO for CSV with BytesIO for PDF generation.

### Source / commands
```text
import csv, io
reader = csv.DictReader(io.StringIO(text))
for row in reader:
    print(row["title"], row["value"])

# Binary download:
return FileResponse(buffer, as_attachment=True, filename="observations.pdf")
```

**Practical route:** `/course/observations/`

**Observation record:** Input / command: __________; result / status: __________; invalid-input result: __________; screenshot reference: __________.

**Result:** Explain what your output demonstrates: __________.

### Viva / post-lab questions
- Why validate all rows before bulk_create? Answer: Avoid partial imports
- Which buffer stores PDF bytes? Answer: BytesIO

## 3.3 — Models, migrations, CRUD and bulk operations

**Aim:** Perform and explain models, migrations, crud and bulk operations using a reproducible laboratory exercise.

**Outcome:** CO3

### Theory
A model defines database fields and relations. makemigrations creates a versioned schema change; migrate applies it. The ORM translates query operations to parameterized SQL. create, filter, update and delete correspond to INSERT, SELECT, UPDATE and DELETE. bulk_create and bulk_update reduce database round trips but do not call each object save() or emit its save signals; validate explicitly. Use transactions for related writes.

### Procedure
1. Run showmigrations and inspect course/migrations/0001_initial.py.
2. Create, edit and delete your observations in the practical.
3. Run the ORM commands in a disposable database or with test records.
4. Inspect a QuerySet.query and compare it with the SQL examples.
5. Read services.import_csv for the validated bulk_create path and run the notebook bulk_update exercise.

### Source / commands
```text
Observation.objects.create(owner=user, title="Latency", value=12)
rows = list(Observation.objects.filter(owner=user))
for row in rows:
    row.notes = "Reviewed"
Observation.objects.bulk_update(rows, ["notes"])
Observation.objects.filter(owner=user, title="Latency").delete()

-- Equivalent CRUD concepts (values should be parameters):
INSERT INTO course_observation (owner_id,title,value,notes,created_at) VALUES (1,'Latency',12,'',CURRENT_TIMESTAMP);
SELECT * FROM course_observation WHERE owner_id=1;
UPDATE course_observation SET notes='Reviewed' WHERE owner_id=1;
DELETE FROM course_observation WHERE owner_id=1;
```

**Practical route:** `/course/observations/`

**Observation record:** Input / command: __________; result / status: __________; invalid-input result: __________; screenshot reference: __________.

**Result:** Explain what your output demonstrates: __________.

### Viva / post-lab questions
- What applies schema changes? Answer: migrate
- Does bulk_update call each save()? Answer: No

## 4.1 — Users, sessions, permissions and groups

**Aim:** Perform and explain users, sessions, permissions and groups using a reproducible laboratory exercise.

**Outcome:** CO4

### Theory
Authentication identifies a user; authorization determines allowed actions. This project defines a custom AbstractUser before its first migration and stores roll_number. Django hashes passwords, rotates session credentials at login, and supports password change and token-based reset. The development email backend prints reset messages to the server console. Each observation belongs to its creator. The instructor export requires an explicit permission; staff access and model permissions are separate concepts.

### Procedure
1. Register two users and create an observation for each.
2. Verify each account sees only its own rows.
3. Change a password, then request a password reset using your registered email.
4. Follow the reset URL printed by the console backend; a token is single-use.
5. Create an Instructors group in admin, assign export_observation and test /course/instructor/export/ with and without it.
6. Use the POST logout button and verify protected routes redirect to login.

### Source / commands
```text
from django.contrib.auth.models import Group, Permission
group, _ = Group.objects.get_or_create(name="Instructors")
permission = Permission.objects.get(codename="export_observation", content_type__app_label="course")
group.permissions.add(permission)
user.groups.add(group)
user.has_perm("course.export_observation")
```

**Practical route:** `/course/register/`

**Observation record:** Input / command: __________; result / status: __________; invalid-input result: __________; screenshot reference: __________.

**Result:** Explain what your output demonstrates: __________.

### Viva / post-lab questions
- How do authentication and authorization differ? Answer: Identity versus allowed actions
- Where do reset emails go in local development? Answer: Server console

## 4.2 — Django administration, filters and actions

**Aim:** Perform and explain django administration, filters and actions using a reproducible laboratory exercise.

**Outcome:** CO4

### Theory
Django admin is a trusted staff interface generated from model metadata. Registering a ModelAdmin controls list columns, search fields, filters and actions. This lab customizes the site headings and user fieldsets, adds owner/date filters and a clear-notes action. Staff users still need model permissions. Admin actions can change many records: inspect the selection before confirming an operation.

### Procedure
1. Create a superuser from the terminal; never commit credentials.
2. Open /admin/ and inspect Users, Groups and Observations.
3. Search observations by title or username and filter by owner.
4. Select test observations and run Clear notes.
5. Create a staff account with view-only permissions and compare its controls.

### Source / commands
```text
python manage.py createsuperuser

@admin.register(Observation)
class ObservationAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "value", "created_at")
    list_filter = ("created_at", "owner")
    search_fields = ("title", "owner__username")
```

**Practical route:** `/admin/`

**Observation record:** Input / command: __________; result / status: __________; invalid-input result: __________; screenshot reference: __________.

**Result:** Explain what your output demonstrates: __________.

### Viva / post-lab questions
- Does is_staff grant every model permission? Answer: No
- Which option creates sidebar filters? Answer: list_filter

## 5.1 — REST endpoints and Pydantic validation

**Aim:** Perform and explain rest endpoints and pydantic validation using a reproducible laboratory exercise.

**Outcome:** CO5

### Theory
REST uses resource URLs and HTTP semantics: GET reads, POST creates (201), PUT replaces, DELETE removes (204), and missing resources return 404. JSON is a representation format. FastAPI builds on ASGI with type-driven validation and OpenAPI documentation. It supports async functions for awaitable I/O; async alone does not accelerate CPU work or blocking database calls. Django REST Framework integrates closely with Django ORM/auth/admin; FastAPI suits a separate typed API. Neither is universally superior. The companion API uses SQLite persistence and Pydantic constraints, not a process-local dictionary.

### Procedure
1. Start the separate FastAPI service on port 8001.
2. Open /docs and inspect the generated schemas.
3. POST an observation, then GET it by its returned integer ID.
4. Filter the collection with the min_value query parameter.
5. Try a short title or negative value and inspect HTTP 422.
6. Replace and delete the resource; verify a subsequent GET returns 404.

### Source / commands
```text
uvicorn api.main:app --port 8001

curl -X POST http://127.0.0.1:8001/observations -H "Content-Type: application/json" -d '{"title":"Latency","value":12}'
curl "http://127.0.0.1:8001/observations?min_value=10"
```

**Practical route:** `http://127.0.0.1:8001/docs`

**Observation record:** Input / command: __________; result / status: __________; invalid-input result: __________; screenshot reference: __________.

**Result:** Explain what your output demonstrates: __________.

### Viva / post-lab questions
- Which status signals schema validation failure? Answer: 422
- What does async help with? Answer: Awaitable I/O concurrency

## 5.2 — Endpoint tests and deployment

**Aim:** Perform and explain endpoint tests and deployment using a reproducible laboratory exercise.

**Outcome:** CO5

### Theory
Tests should assert status codes, response fields, persistence and error cases. FastAPI TestClient runs the ASGI app without a network server. This repository uses an isolated temporary SQLite database per test. Django tests check validation, ownership, permissions, CSV atomicity, authentication and rendered pages. Deployment needs a production server, private database volume, secret configuration, HTTPS and static serving. The supplied container and guide are a reproducible starting point; a successful local run does not prove a hosted deployment.

### Procedure
1. Run the Django tests and FastAPI pytest suite.
2. Read tests for 201 creation, 422 validation and 404 missing records.
3. Run check, migration drift check and collectstatic.
4. Build the Docker image and run Django using the documented environment variables.
5. Follow docs/deployment.md for HTTPS, static serving, volumes and a release checklist.

### Source / commands
```text
python manage.py test
python -m pytest api/tests.py -q
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py collectstatic --noinput
docker build -t django-vlab .
```

**Practical route:** `/course/`

**Observation record:** Input / command: __________; result / status: __________; invalid-input result: __________; screenshot reference: __________.

**Result:** Explain what your output demonstrates: __________.

### Viva / post-lab questions
- What should an endpoint test verify? Answer: Status and response data
- Why isolate the test database? Answer: Prevent tests altering real observations

## References and boundaries
- [Django 5.2 documentation](https://docs.djangoproject.com/en/5.2/)
- [FastAPI tutorial and tests](https://fastapi.tiangolo.com/tutorial/testing/)
- [Python csv](https://docs.python.org/3/library/csv.html)
- [Pro Git: Git on the server](https://git-scm.com/book/en/v2/Git-on-the-Server-The-Protocols)
- [React JSX](https://react.dev/learn/writing-markup-with-jsx)
- [Virtual Labs section reference](https://se-iitkgp.vlabs.ac.in/exp/problem-statements/exercise_index.html)

The course text is original teaching material, not a copied official laboratory. The supplied syllabus is the mapping authority. The UI follows the reference structure without claiming institutional affiliation. A hosted Git server and HTTPS deployment are documented exercises; no external server is provisioned by the notebook. Password-reset mail uses the console locally; SMTP delivery must be configured and verified separately.
