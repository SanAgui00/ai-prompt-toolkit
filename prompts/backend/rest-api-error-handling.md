# REST API Global Error Handler

**Model:** Claude Sonnet 4.6 / GPT-4o
**Category:** backend
**Variables:** `{{PACKAGE}}`, `{{APP_NAME}}`

---

Generate a global exception handling setup for a Spring Boot REST API in package `{{PACKAGE}}`.

**1. Standard error response body** (`ApiError.java`):
- Fields: `timestamp` (ISO-8601), `status` (int), `error` (String), `message` (String), `path` (String)
- Use Lombok `@Builder`, `@Getter`
- Include a static factory method `ApiError.of(HttpStatus, String, String)`

**2. Global exception handler** (`GlobalExceptionHandler.java`):
- Annotated with `@RestControllerAdvice`
- Handle the following with correct HTTP status:
  - `ResourceNotFoundException` → 404
  - `MethodArgumentNotValidException` → 400 (collect all field errors into message)
  - `HttpMessageNotReadableException` → 400
  - `DataIntegrityViolationException` → 409 (detect duplicate key)
  - `AccessDeniedException` → 403
  - `Exception` (fallback) → 500 (log stack trace, hide internals in response)
- Inject `HttpServletRequest` to include path in response
- Use `@Slf4j` for logging

**3. Usage example** (in a comment block):
Show how `ResourceNotFoundException` is thrown from a service and how the JSON response looks to the API consumer.

Output each class in a separate labeled code block.
