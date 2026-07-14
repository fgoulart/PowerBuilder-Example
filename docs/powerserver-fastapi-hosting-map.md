# PowerServer → FastAPI hosting map

Destination clones aren't under `/app`; I'll resolve fixtures and backend paths from the monorepo root.

### [JAMES_JIRA_AGENTIC] [Modernization] PowerServer Web API as primary strangler-fig replatform path to .NET 6 cloud hosting - FastAPI hosting ops parity (URL, timeouts, secrets, health)

**Type:** Modernization / migration (strangler-fig replatform)

**Labels:** `james-agentic`, `modernization`, `backend`, `infrastructure`, `powerserver-strangler`, `fastapi`, `docker`

**Dependencies:** None (informational prerequisite: origin feature `delivery-nt-makefile-build` for PBL artifact consistency—do not port to destination)

1. Externalize hosting config in `Settings` (replace any implicit `localhost:5088` mindset with env-driven `PUBLIC_API_URL` / bind host/port / HTTPS flag).

## Contract table

| Origin PowerServer | Destination FastAPI |
|--------------------|---------------------|
| Web API URL/port (demo 5088) | `PUBLIC_API_URL` default `http://localhost:8000`, `BIND_HOST`/`BIND_PORT` |
| Session/request/transaction timeouts 3600/3600/120 | `SESSION_TIMEOUT_SECONDS` / `REQUEST_TIMEOUT_SECONDS` / `TRANSACTION_TIMEOUT_SECONDS` |
| Appeon license import | `APPEON_LICENSE_KEY` or `LICENSE_KEY` via `license_gate` (presence/format only) |
| SQL Anywhere (+ optional Postgres) | **Postgres-only**; SQL Anywhere retired |
| Manual/IIS health | `GET /api/v1/health` enriched for readiness. |

## RuntimeModules capability matrix (deferred)

Origin Examples RuntimeModules often leave REST/browser support disabled. Treat module parity as deferred; do not block hosting/ops on those capabilities.

## Smoke

```bash
curl -sf http://localhost:8000/api/v1/health
```

Demo Compose credentials (`postgres`/`postgres`) are for local smoke only—not production-safe.
