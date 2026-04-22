# GitHub Actions CI Pipeline for Java / Spring Boot

**Model:** Claude Sonnet 4.6 / GPT-4o
**Category:** devops
**Variables:** `{{JAVA_VERSION}}`, `{{ECR_REGISTRY}}`, `{{ECR_REPO}}`, `{{AWS_REGION}}`

---

Generate a GitHub Actions workflow file (`.github/workflows/ci.yml`) for a Java Spring Boot project.

Requirements:
- **Trigger:** on push to `main` and `develop`, and on pull requests to `main`
- **Jobs:**
  1. **test** — Checkout, setup JDK `{{JAVA_VERSION}}` (temurin distribution), cache Maven `~/.m2`, run `mvn verify`
  2. **build-and-push** — Runs only on push to `main`, depends on `test`. Steps:
     - Configure AWS credentials via `aws-actions/configure-aws-credentials@v4` using GitHub secrets `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`
     - Login to Amazon ECR `{{ECR_REGISTRY}}`
     - Build Docker image tagged with `{{ECR_REGISTRY}}/{{ECR_REPO}}:${{ github.sha }}`
     - Push image to ECR
     - Output the full image URI as a job summary
- Use `actions/checkout@v4` and `actions/setup-java@v4`
- Add concurrency group to cancel in-progress runs on the same branch
- Include comments explaining each step

Also provide:
1. A list of required GitHub repository secrets and their descriptions
2. A badge snippet for the README showing workflow status
