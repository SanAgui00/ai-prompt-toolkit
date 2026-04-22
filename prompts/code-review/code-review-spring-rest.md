# Spring Boot REST Controller Code Review

**Model:** Claude Sonnet 4.6 / GPT-4o
**Category:** code-review
**Variables:** `{{CONTROLLER_CODE}}`, `{{ENTITY}}`, `{{FRAMEWORK_VERSION}}`

---

Review the following Spring Boot REST controller for `{{ENTITY}}` (Spring Boot `{{FRAMEWORK_VERSION}}`):

```java
{{CONTROLLER_CODE}}
```

Evaluate across these axes and provide findings with line references where possible:

1. **Correctness**
   - HTTP status codes match REST semantics (201 for POST, 204 for DELETE, 404 for missing resources)
   - Error responses use a consistent structure (e.g., ProblemDetail or custom ErrorResponse)
   - No business logic leaking into the controller layer

2. **Security**
   - Input validation via `@Valid` / `@Validated` on request bodies and path variables
   - No sensitive data (passwords, tokens) exposed in response bodies or logs
   - Proper authorization annotations (`@PreAuthorize`, `@Secured`) or note their absence
   - No direct entity exposure (DTOs used, not JPA entities)

3. **Readability & Conventions**
   - Consistent naming (camelCase methods, kebab-case URL paths)
   - Swagger/OpenAPI annotations present (`@Operation`, `@ApiResponse`, `@Tag`)
   - No commented-out code or TODO left in production paths

4. **Performance**
   - Pagination used for list endpoints (not returning unbounded collections)
   - No N+1 query triggers visible at controller level
   - Response compression or caching annotations where appropriate

5. **Testability**
   - Constructor injection used (no field `@Autowired`)
   - No static calls or hidden dependencies that make unit testing hard

**Output format:**
- Summary table: axis → Severity (OK / WARN / FAIL) + one-line finding
- Detailed findings: each issue with severity, description, and a corrected code snippet
- Overall verdict: APPROVE / REQUEST CHANGES + top 3 action items
