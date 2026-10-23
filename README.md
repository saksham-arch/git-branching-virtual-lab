# Django and Python Virtual Laboratory

A teaching laboratory mapped to **SVU–KJSCE 2023_1.0, TY B Tech COMP BoS, pages 80–81**. All 13 units across five modules have an experiment page, theory, procedure, practical workspace or reproducible terminal exercise, observations and assessment. The original Git branching and conflict-resolution experiment remains at `/`.

The interface follows the section-based Virtual Labs format. This is an independent academic project, not an official institutional website.

## Run

Python 3.13 is the tested interpreter. Django 5.2 LTS is used. `requirements.txt` declares supported ranges; `requirements.lock` pins the tested environment.

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.lock
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000/course/> for the course or <http://127.0.0.1:8000/> for the Git simulation. Register your own account to use the observation practical. Create an administrator with `python manage.py createsuperuser`; no shared credentials are shipped.

A new `course.sqlite3` stores accounts and observations. Any previous `db.sqlite3` is left untouched. Set `DJANGO_DB_PATH` to select another database before running migrations. The custom user model must exist from the first migration in a fresh database.

## Practical work

| Area | Route / source |
|---|---|
| All experiments and syllabus units | `/course/` |
| Original Git simulator and command exercise | `/` |
| Function and class views, template context/filters, verbatim, local JS | `/course/templates/` |
| Real React/JSX component served as Django static assets | `/course/react/`, `frontend/src/main.jsx` |
| Forms, create/read/update/delete and graph | `/course/observations/` |
| Validated atomic CSV import | `/course/csv/import/` |
| CSV and PDF downloads | `/course/csv/export/`, `/course/pdf/` |
| Registration, login/logout, password change and reset | `/course/register/`, `/accounts/` |
| Group permission example | `/course/instructor/export/` |
| Custom admin, user fields, search, filters, action | `/admin/` |
| Separate persistent FastAPI REST practical | `api/main.py` |

Measurements belong to their creator. The instructor export requires `course.export_observation`, assignable through a group in admin. Password reset messages print to the local server console; SMTP delivery is a separate deployment configuration. CSV imports accept at most 500 records / 1 MB and reject an invalid batch without partial writes. CSV exports neutralize formula prefixes.

### React/JSX

The compiled local bundle is included, so `/course/react/` works without npm or a CDN. To change the JSX source, use Node 22.12+:

```bash
cd frontend
npm ci
npm run build
cd ..
mkdir -p lab/static/react
cp -R frontend/dist/. lab/static/react/
```

Django renders the page shell and serves the built ES module with the `static` template tag. Vite compiles JSX to JavaScript; no browser Babel transpiler is used. The verbatim demonstration is separate so the server/client delimiter boundary is visible.

### FastAPI

In another terminal with the same environment:

```bash
uvicorn api.main:app --host 127.0.0.1 --port 8001
```

Open <http://127.0.0.1:8001/docs>. The API supports POST, GET, PUT and DELETE `/observations`, path and query validation, JSON response schemas, 201/204/404/422 semantics and SQLite persistence. `FASTAPI_DB_PATH` selects its database. This deliberately separate teaching service has no authentication; bind it to loopback. Django accounts do not authorize API calls. Swagger assets require internet access; `/openapi.json` does not.

## Notebook and academic record

- [Syllabus mapping and full experiment record](docs/syllabus-and-lab-record.md): all supplied units, CO mapping, module hours, theory, procedures, source pointers, viva answers and observation blanks.
- [Runnable notebook](notebooks/svu-kjsce-laboratory.ipynb): representative assertions for each implemented area, using a disposable database.
- [Sample CSV](docs/sample-observations.csv).
- [Deployment guide](docs/deployment.md): container, Gunicorn, HTTPS/static/data configuration and release checks.

To open the notebook, install `jupyterlab` and `ipykernel` into the environment and select that kernel. It can be run from the repository root or `notebooks/`. It does not claim to perform external server provisioning or browser tasks for you.

## Verify

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
python -m pytest api/tests.py -q
python manage.py findstatic lab/course.css --verbosity 2
python manage.py collectstatic --noinput
```

Tests cover validation, ownership, CSRF, password workflows, group permissions, admin rendering, CSV atomicity, PDF output, API persistence and error responses. Git server commands are scoped to a disposable practice directory. See [verification notes](docs/verification.md) for the actual checks performed for this revision.

## Sources

Syllabus text supplied with the assignment. Framework references: [Django 5.2](https://docs.djangoproject.com/en/5.2/), [FastAPI](https://fastapi.tiangolo.com/), [Python csv](https://docs.python.org/3/library/csv.html), [React JSX](https://react.dev/learn/writing-markup-with-jsx), [Pro Git](https://git-scm.com/book/en/v2). Section/navigation reference: [Virtual Labs software engineering experiment](https://se-iitkgp.vlabs.ac.in/exp/problem-statements/exercise_index.html).
