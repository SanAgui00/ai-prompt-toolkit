# Kubernetes Deployment Manifest Generator

**Model:** Claude Sonnet 4.6 / GPT-4o
**Category:** devops
**Variables:** `{{APP_NAME}}`, `{{IMAGE}}`, `{{PORT}}`, `{{REPLICAS}}`, `{{HPA_MAX_REPLICAS}}`, `{{NAMESPACE}}`

---

Generate production-ready Kubernetes manifests for deploying `{{APP_NAME}}` in namespace `{{NAMESPACE}}`.

Generate the following resources in a single YAML file separated by `---`:

1. **Namespace** — `{{NAMESPACE}}` with label `app: {{APP_NAME}}`
2. **Deployment:**
   - `replicas: {{REPLICAS}}`
   - Image: `{{IMAGE}}`
   - Container port: `{{PORT}}`
   - Resource requests/limits: CPU `100m`/`500m`, Memory `256Mi`/`512Mi`
   - `livenessProbe` and `readinessProbe` on `/actuator/health` (HTTP GET, port `{{PORT}}`) with appropriate `initialDelaySeconds`, `periodSeconds`
   - `RollingUpdate` strategy: `maxSurge: 1`, `maxUnavailable: 0`
   - Environment variables from a `ConfigMap` and a `Secret` (generate their names as `{{APP_NAME}}-config` and `{{APP_NAME}}-secret`)
   - `securityContext`: `runAsNonRoot: true`, `readOnlyRootFilesystem: true`, `allowPrivilegeEscalation: false`
3. **Service** — `ClusterIP`, port `80` → targetPort `{{PORT}}`
4. **HorizontalPodAutoscaler** — min `{{REPLICAS}}`, max `{{HPA_MAX_REPLICAS}}` (recommended: REPLICAS × 3, e.g. REPLICAS=2 → HPA_MAX_REPLICAS=6), target CPU utilization `70%`
5. **ConfigMap** — `{{APP_NAME}}-config` with placeholder keys `SPRING_PROFILES_ACTIVE` and `SERVER_PORT`
6. **Secret** — `{{APP_NAME}}-secret` with placeholder base64 keys `DB_PASSWORD` and `API_KEY`

Also provide:
1. `kubectl apply` command to deploy all manifests
2. `kubectl rollout status` command to verify the deployment
