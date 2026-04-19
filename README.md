# FastAPI Template with Docker Deploy

Template project for running and deploying FastAPI with Docker Compose, local Registry, and Watchtower auto-update.

## Project layout

- `app/main.py` - FastAPI app with `/` and `/health`
- `app/Dockerfile` - production-ready container image
- `app/Makefile` - build/push helpers
- `docker-compose.yml` - app + registry + watchtower stack
- `.env.example` - deployment environment template

## Quick start

1. Create env file:
   - `copy .env.example .env` (Windows)
2. Run stack:
   - `docker compose up -d`
3. Check app:
   - `http://localhost:8000/health`

## Build and deploy image

From `app` directory:

- Login to registry:
  - `make login REGISTRY_USER=<user> REGISTRY_PASSWORD=<pass>`
- Build and push:
  - `make bp VERSION=v1`

## Notes

- For local development this setup uses HTTP registry mode.
- For production, configure TLS certificates and strong credentials.
