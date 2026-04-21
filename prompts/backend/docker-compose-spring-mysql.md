# Docker Compose — Spring Boot + MySQL

**Model:** Claude Sonnet 4.6 / GPT-4o
**Category:** backend
**Variables:** `{{APP_NAME}}`, `{{DB_NAME}}`, `{{DB_USER}}`, `{{DB_PASSWORD}}`, `{{APP_PORT}}`

---

Generate a production-ready Docker setup for a Spring Boot application with MySQL.

**1. `Dockerfile`** (multi-stage build):
- Stage 1 (`build`): Use `eclipse-temurin:21-jdk-alpine`, copy pom.xml + src, run `mvn package -DskipTests`
- Stage 2 (`runtime`): Use `eclipse-temurin:21-jre-alpine`, copy jar from build stage
- Run as non-root user (`appuser`)
- Expose `{{APP_PORT}}`
- Set `JAVA_OPTS` env var for JVM tuning (heap size)
- Add `HEALTHCHECK` using curl on `/actuator/health`

**2. `docker-compose.yml`**:
- Services: `app` (Spring Boot) + `db` (MySQL 8.0)
- `app` depends on `db` with `condition: service_healthy`
- MySQL healthcheck: `mysqladmin ping`
- Named volumes for MySQL data persistence
- Environment variables for DB connection pulled from `.env`
- Network: custom bridge network isolating both services
- Restart policy: `unless-stopped` on both

**3. `.env.example`**:
- All required variables with placeholder values and comments
- Include: DB credentials, app port, Spring profile, JVM opts

**4. `.dockerignore`**:
- Exclude: `target/`, `.git/`, `*.md`, `.env`, `*.log`

**5. `application-docker.properties`**:
- Spring datasource pointing to `db` service hostname
- Connection pool settings (HikariCP: min 2, max 10)
- Actuator health endpoint enabled

Output each file in a separate labeled code block.
