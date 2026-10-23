# Verification record

Checks for this revision are recorded here after execution. The GitHub Actions workflow runs Django checks/tests, FastAPI tests, static collection, the notebook runner and the JSX build on Ubuntu/Python 3.13/Node 22.

Local verification uses macOS. Native package loading on this host stalled during initial verification; Linux CI provides an independent execution environment for those checks. Browser checks use the actual local Django server.

Hosted deployment, SMTP delivery and a production Git server are separate exercises and are not claimed as completed infrastructure.
