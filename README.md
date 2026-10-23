# Git Branching, Merging and Conflict Resolution — Virtual Lab

The original Git virtual laboratory, extended with accounts, saved practice attempts, CSV/PDF records, quiz history and a React merge-prediction exercise. The aim, original navigation, graph simulation, command lab, conflict editor and assessments remain the project’s core.

The supplied Django/Python topics are an [implementation checklist](docs/implementation-checklist.md) for this single problem statement. They are not separate experiments.

## Run

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.lock
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000/>. The legacy `/course/` URL redirects to the original experiment.

## Extensions to the same experiment

- **My lab record:** register or sign in, then record branch names, quiz percentages, commands and conflict-resolution notes. Edit/delete your own attempts, import batches, compare quiz scores and download CSV/PDF.
- **Quiz persistence:** the existing Git quiz offers a save-attempt button. The authenticated Django endpoint validates and stores the result.
- **Merge prediction:** a local React/JSX practical asks whether a branch history permits a fast-forward or requires a merge commit, then links back to the original simulation.
- **Administration:** create a superuser with `python manage.py createsuperuser`. Search/filter practice records and use admin actions. Assign `course.export_observation` through an instructor group to enable class export.
- **Password management:** Django login/logout, change and reset workflows. Development reset messages print to the server console; production email requires SMTP configuration.

`course.sqlite3` stores Django accounts/records. The internal record model retains its original migration name to preserve data. `title` means branch/attempt label, `value` means quiz percentage and `notes` means commands/resolution notes. CSV columns remain `title,value,notes`; [sample records](docs/sample-observations.csv) use this schema.

## Companion API

```bash
uvicorn api.main:app --host 127.0.0.1 --port 8001
```

Open <http://127.0.0.1:8001/docs>. `/observations` represents Git practice records and supports POST/GET/PUT/DELETE, path/query validation and persistent SQLite storage. This independent teaching API has no authentication and uses a separate database. Keep it on loopback. The original experiment saves signed-in attempts through Django instead.

## JSX source

The compiled assets are included under lab/static/react/. To change the merge-prediction component, use Node 22.12+:

```bash
cd frontend
npm ci
npm run build
cd ..
cp -R frontend/dist/. lab/static/react/
```

## Documentation and verification

- [Implementation checklist](docs/implementation-checklist.md)
- [Runnable Git laboratory notebook](notebooks/git-laboratory.ipynb), using disposable data
- [Git server and remote practice](docs/git-server-practical.md)
- [Deployment guide](docs/deployment.md)

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
python -m pytest api/tests.py -q
python notebooks/run_notebook.py
python manage.py findstatic lab/app.js --verbosity 2
python manage.py collectstatic --noinput
```

The interface is inspired by Virtual Labs and is an independent academic implementation. No institutional affiliation is claimed. Docker build and local tests do not establish live hosting, SMTP delivery or a provisioned SSH Git server.
