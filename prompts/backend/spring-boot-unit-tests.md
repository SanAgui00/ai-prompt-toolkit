# Spring Boot Service Unit Test Generator

**Model:** Claude Sonnet 4.6 / GPT-4o
**Category:** backend
**Variables:** `{{ENTITY}}`, `{{PACKAGE}}`, `{{SERVICE_CLASS}}`, `{{REPO_CLASS}}`

---

Generate a complete JUnit 5 unit test suite for `{{SERVICE_CLASS}}` in package `{{PACKAGE}}`.

Setup:
- Use `@ExtendWith(MockitoExtension.class)` — no Spring context
- Mock `{{REPO_CLASS}}` with `@Mock`
- Inject via `@InjectMocks`

Write tests for each of these scenarios:

**findById:**
- Returns DTO when entity exists
- Throws `ResourceNotFoundException` when entity not found

**findAll (paginated):**
- Returns page of DTOs mapped correctly
- Returns empty page when no records exist

**create:**
- Saves entity and returns response DTO with generated ID
- Verify `repository.save()` called exactly once

**update:**
- Updates existing entity fields and returns updated DTO
- Throws `ResourceNotFoundException` when entity not found

**delete:**
- Calls `repository.deleteById()` when entity exists
- Throws `ResourceNotFoundException` when entity not found

Standards:
- Use `@DisplayName` with descriptive test names (Given/When/Then format)
- Use `assertThat` from AssertJ (not JUnit assertions)
- Use `ArgumentCaptor` on at least one test to verify saved entity state
- Group tests in `@Nested` classes by method name
- Mock data via static factory methods or builders — no magic numbers

Output as a single test class with all nested groups.
