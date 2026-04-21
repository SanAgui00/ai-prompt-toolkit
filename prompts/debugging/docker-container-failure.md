# Docker Container Failure Debugger

**Model:** Claude Sonnet 4.6 / GPT-4o
**Category:** debugging
**Variables:** `{{CONTAINER_LOGS}}`, `{{DOCKERFILE}}`, `{{COMPOSE_FILE}}`

---

A Docker container is failing to start or crashing at runtime.

**Container logs:**
```
{{CONTAINER_LOGS}}
```

**Dockerfile:**
```dockerfile
{{DOCKERFILE}}
```

**docker-compose.yml (if applicable):**
```yaml
{{COMPOSE_FILE}}
```

Diagnose and fix:
1. **Failure type** — startup crash, OOM kill, healthcheck failure, network issue, or permission error
2. **Root cause** — exact line in logs or config that indicates the problem
3. **Fix** — corrected Dockerfile or compose config with explanation
4. **Verification command** — the exact `docker` command to confirm the fix worked
5. **Prevention** — one best practice to avoid this class of error (e.g., multi-stage builds, non-root user, explicit HEALTHCHECK)
