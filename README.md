# campus-loan-service

Loan Service for the Campus IT Loan System.

## Development setup

Install Python 3.14 or newer and uv, then run:

```sh
uv sync
```

This installs `fastapi[standard]`, including the FastAPI CLI and Uvicorn, into the
local `.venv` using `uv.lock`.

## Run locally

```sh
uv run fastapi dev
```

The development server listens on `http://127.0.0.1:8000`. Test the public health
check from another terminal:

Expected response: `{"status":"ok"}` with HTTP 200. This checks that the API is
running; it does not check database readiness or external dependencies.
Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

The application currently exposes only the health check. Domain use cases and
persistence adapters have not been implemented.