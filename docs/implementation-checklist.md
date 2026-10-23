# Git laboratory implementation checklist

The problem statement remains **Git Branching, Merging and Conflict Resolution**. The supplied Django/Python topics are implementation requirements for that one project. They are not a course catalog or a list of new experiments.

| Requirement | Implementation in this Git laboratory |
|---|---|
| Django environment, dependencies, structure and development server | manage.py, gitlab_project/, requirements.txt and pinned requirements.lock; README run commands |
| JavaScript library, JSX and verbatim | Original vanilla JS simulation plus the React merge-prediction practical in frontend/src/main.jsx; course/react.html preserves client delimiters with verbatim |
| Git/GitHub, local/hosted server, remotes, branches and merges | Original command lab, graph and conflict editor; docs/git-server-practical.md supplies two-clone and server procedures |
| URL mapping, function views and class views | lab/views.py experiment FBV, course/views.py TemplateLab CBV and named URL routes |
| Dynamic templates, context variables and filters | Authenticated Git records rendered from view context; template inheritance, loops, empty state and length filter on record count |
| Static tags, finders, FileSystemFinder and findstatic | Existing app/static directories and static template tags; Django default finders include FileSystemFinder and AppDirectoriesFinder. Run findstatic and collectstatic as documented below |
| Forms, Python cleaned values, custom validation, placeholders and initial values | Git practice-record ModelForm: branch/attempt name, Decimal quiz score from 0–100 and conflict notes; initial score and placeholders; CSRF and successful POST redirect |
| CSV and graphs | Atomic validated batch import, csv.DictReader/csv.writer, per-learner quiz score graph and tabular values |
| PDF and binary files | Downloadable Git practice record generated into BytesIO and streamed with FileResponse |
| SQL, ORM, models, migrations, CRUD and bulk operations | Existing User and record tables, migrations, owner-scoped create/read/edit/delete, validated bulk_create import, notebook bulk_update; parameterized SQL example below |
| Registration/login/logout and password management/reset | Django auth routes and course account pages; console reset email in development |
| Groups, permissions and custom user | Custom User; per-learner ownership and explicit instructor export permission assignable via groups |
| Admin models/actions/filters/UI | Git lab admin headings, user fieldsets, record owner/date filters, search and clear-notes action |
| FastAPI vs DRF, REST semantics, async and automatic docs | api/main.py companion Git record service; typed JSON, path/query fields, GET/POST/PUT/DELETE, 201/204/404/422, async health and OpenAPI /docs |
| Pydantic validation and endpoint tests | Score limits, nonempty branch/attempt title, finite numeric data; api/tests.py status, body, persistence and error checks |
| Deployment | Docker/Gunicorn build and docs/deployment.md; live hosting remains an explicit infrastructure task |

## Static finder verification

```bash
python manage.py findstatic lab/app.js --verbosity 2
python manage.py collectstatic --noinput
python manage.py shell -c 'from django.conf import settings; print(settings.STATICFILES_FINDERS)'
```

For the FileSystemFinder exercise, set `STATICFILES_DIRS` to a separate project asset directory, add a file there, and rerun findstatic. App assets use AppDirectoriesFinder by default; no extra STATICFILES_DIRS folder is needed for the shipped app.

## SQL and ORM

The record model retains the internal class name Observation to preserve existing migrations and student data. The interface calls these Git practice records. `title` stores a branch/attempt label and `value` stores a quiz percentage.

```python
from django.db import connection
from course.models import Observation
record = Observation.objects.create(owner=user, title='feature/navbar', value=75, notes='Resolved conflict')
record.notes = 'Verified with git status and git log'
record.save()
with connection.cursor() as cursor:
    cursor.execute('SELECT title, value FROM course_observation WHERE owner_id = %s', [user.pk])
    print(cursor.fetchall())
Observation.objects.filter(pk=record.pk, owner=user).delete()
```

Bulk ORM operations skip per-object save/signals. Import validates each row first; the notebook exercises bulk_update. The API uses parameterized SQLite INSERT/SELECT/UPDATE/DELETE for the same domain resource in a separate database.

## API design choice

FastAPI is useful here as a separate typed teaching API with automatic OpenAPI documentation. DRF would instead integrate tightly with Django ORM and authentication; neither is universally better. Async handlers benefit awaitable I/O; they do not make blocking SQLite or CPU work asynchronous. Synchronous CRUD handlers use the framework thread pool.

The companion API is loopback-only and unauthenticated. It does not share Django accounts or its database. The original browser quiz saves through the authenticated Django endpoint, never through this companion API.
