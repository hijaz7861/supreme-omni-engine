# Supreme Omni Engine

**Maintainer:** M Naeem Khan (hijaz7861)

Supreme Omni Engine is currently at its web-application foundation stage. This repository provides a Flask service, health/status endpoints, and a Render deployment definition. It does not yet contain a completed AI orchestration engine or claim model execution.

## Current capabilities

- Flask web service with a simple status page.
- GET /healthz liveness endpoint for hosting-platform health checks.
- GET /api/status machine-readable implementation and configuration status.
- Gunicorn production entry point.
- GitHub Actions CI for automated tests and Python compilation.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app_web.py
```

Open http://127.0.0.1:5000, or inspect /healthz and /api/status.

## Configuration

- PORT: optional web server port (defaults to 5000).
- GEMINI_API_KEY: recognized as a configured integration flag only. No Gemini request is made yet, and the value is never returned by the status endpoint.

Set secrets in the hosting provider's secret/environment settings. Never commit API keys.

## Tests

```bash
pip install pytest
pytest -q
python -m compileall -q app_web.py tests
```

GitHub Actions runs these checks on pushes and pull requests targeting main. It does not create issues, run on a six-hour schedule, or require issue-write permissions.

## Repository sync

automate.sh only pushes from the local main branch and uses a normal fast-forward-safe push. It deliberately does not force-push or rename branches.

## Engineering roadmap

1. Define supported tasks, model providers, tool interfaces, and security boundaries.
2. Implement provider adapters and orchestration behind explicit interfaces.
3. Add authentication, authorization, rate limits, audit logs, and secret management before exposing execution endpoints.
4. Add unit, integration, and failure-mode tests for each engine subsystem.
5. Add deployment and observability only after runtime behavior is implemented and verified.

No production AI execution, external integration, or hardware capability is claimed until implemented and tested.
