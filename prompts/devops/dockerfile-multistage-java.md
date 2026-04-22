# Multi-Stage Dockerfile for Java / Spring Boot

**Model:** Claude Sonnet 4.6 / GPT-4o
**Category:** devops
**Variables:** `{{APP_NAME}}`, `{{JAR_NAME}}`, `{{JAVA_VERSION}}`, `{{PORT}}`

---

Generate a production-ready multi-stage Dockerfile for a Spring Boot application named `{{APP_NAME}}`.

Requirements:
- **Stage 1 — build:** Use `maven:3-eclipse-temurin-{{JAVA_VERSION}}` as base. Copy `pom.xml` first, then source. Run `mvn package -DskipTests`. Cache dependency layer separately from source.
- **Stage 2 — runtime:** Use `eclipse-temurin:{{JAVA_VERSION}}-jre-alpine`. Copy only the JAR (`{{JAR_NAME}}.jar`) from the build stage.
- Security hardening:
  - Create a non-root user (`appuser`) and run as that user
  - Set `JAVA_OPTS` env var for heap tuning (default: `-Xms256m -Xmx512m`)
  - Add `HEALTHCHECK` using `/actuator/health` endpoint
- Expose port `{{PORT}}`
- Set `ENTRYPOINT` using exec form (not shell form)
- Add labels: `maintainer`, `version`, `app`

Also provide:
1. A `.dockerignore` file excluding `target/`, `.git/`, `*.md`, and IDE files
2. A one-liner `docker build` command and a `docker run` command with port mapping and env var override example
