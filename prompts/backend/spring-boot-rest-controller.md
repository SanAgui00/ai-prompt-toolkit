# Spring Boot REST Controller Generator

**Model:** Claude Sonnet 4.6 / GPT-4o
**Category:** backend
**Variables:** `{{ENTITY}}`, `{{PACKAGE}}`, `{{ID_TYPE}}`

---

Generate a production-ready Spring Boot REST controller for the entity `{{ENTITY}}` in package `{{PACKAGE}}`.

Requirements:
- Full CRUD endpoints: GET (list + by id), POST, PUT, DELETE
- Use `{{ID_TYPE}}` as the ID type (e.g., Long, UUID)
- Inject service via constructor (no @Autowired on field)
- Use `ResponseEntity<>` with appropriate HTTP status codes:
  - POST → 201 Created with Location header
  - GET list → 200 OK
  - GET by id → 200 OK or 404 Not Found
  - PUT → 200 OK or 404 Not Found
  - DELETE → 204 No Content
- Accept and return DTOs, not entities
- Add `@Valid` on request body parameters
- Include `@RestController`, `@RequestMapping("/api/v1/{{ENTITY_PLURAL}}")`, `@RequiredArgsConstructor`
- Add Swagger/OpenAPI annotations: `@Tag`, `@Operation`, `@ApiResponse`

Also generate:
1. `{{ENTITY}}RequestDTO` — fields with Bean Validation annotations
2. `{{ENTITY}}ResponseDTO` — fields for response
3. `{{ENTITY}}Service` interface with the same CRUD method signatures
4. Stub `{{ENTITY}}ServiceImpl` implementing the interface (TODOs for business logic)

Output each class in a separate code block labeled with the filename.
