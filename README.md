# FioTrix

FastAPI task API with SQLAlchemy and PostgreSQL. Interactive docs are at `/docs`.

```bash
cp .env.example .env
uv sync
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Install with pip via `requirements.txt`. Production runs gunicorn under `systemd/fiotrix.service`.
