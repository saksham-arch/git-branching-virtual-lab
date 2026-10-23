# Verification record

Verified on 23 October 2026.

## Automated execution

[GitHub Actions run 39901886187](https://github.com/saksham-arch/git-branching-virtual-lab/actions/runs/39901886187) passed on Ubuntu with Python 3.13 and Node 22:

- 11 Django tests: all experiment pages and scoring, template escaping/verbatim, forms/CRUD and ownership, CSV atomicity and formula protection, PDF response, group permissions/admin, registration/login/logout/password change/reset and token reuse, CSRF enforcement.
- 7 FastAPI tests: resource lifecycle, body/query/path validation, missing resources, OpenAPI/docs, persistence across clients.
- All 14 Python cells in the notebook executed successfully; committed notebook outputs come from that run.
- Django system check and migration drift check passed; static collection succeeded.
- React/JSX production build succeeded. Its built static assets are committed for direct use without npm.
- Docker image built successfully with Gunicorn and collected static assets.

The final commit adds the already verified built assets, executed notebook and this record. CI also reruns against the final commit.

## Local browser checks

Actual Django server on loopback, not a static mock:

- Course table renders all 13 syllabus units with CO1–CO5.
- Server context renders Asha and the ASHA filter; the verbatim text remains literal.
- Browser JavaScript counter and compiled React counter both increment.
- Course login template renders correctly; a disposable review account can sign in.
- Saving a measurement redirects, shows its success message and persists a table row with value 4.25.
- Measurement graph and table render together.
- Layout inspected at the default narrow viewport and at 1280 × 1000.

Local Django check, migration drift check, static collection, selected page tests and the full password workflow test also passed. The macOS host stalled when loading newly installed native dependencies; full API/PDF/notebook/JSX checks were therefore executed in Linux CI. This is recorded rather than representing CI output as a local run.

## Infrastructure boundaries

No live public application, SMTP provider or external SSH Git server was provisioned. Their setup and verification procedures are documented in deployment.md and git-server-practical.md. FastAPI is intentionally an unauthenticated loopback teaching service with its own database, separate from Django accounts. Docker build success does not establish HTTPS, email delivery or production readiness.
