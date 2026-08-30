# Git Branching, Merging and Conflict Resolution — Virtual Lab

A Django-powered, client-heavy responsive learning experiment inspired by the Virtual Labs interface. Django serves the experiment and JSON metadata API, while browser-side JavaScript powers commit graphs, a conflict editor, assessments, and locally saved progress.

## Run locally

Create the environment and run Django:

```bash
python3.13 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python manage.py migrate
.venv/bin/python manage.py runserver
```

Then visit <http://localhost:8000>.

## Features

- Virtual Labs-inspired responsive layout and experiment navigation
- Interactive branch and merge commit graph
- Guided six-step Git command terminal with hints and validation
- Conflict-resolution validation exercise
- Pretest and scored quiz
- Practical completion checklist
- Learning objectives, prerequisites, full procedure, and further readings
- Browser-local progress persistence
- Accessible semantic controls and mobile navigation

## Technology

Django, HTML, CSS, and vanilla JavaScript. Django owns routing, template/static delivery, health checks, and experiment metadata; simulations stay responsive by running in the browser.

## Django routes

- `/` — rendered experiment
- `/api/experiment/` — experiment metadata JSON
- `/health/` — framework health check

Run verification with `.venv/bin/python manage.py check` and `.venv/bin/python manage.py test`.
