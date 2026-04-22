# Angular HTTP Service Generator

**Model:** Claude Sonnet 4.6 / GPT-4o
**Category:** frontend
**Variables:** `{{SERVICE_NAME}}`, `{{ENTITY}}`, `{{API_BASE_URL}}`, `{{ID_TYPE}}`

---

Generate a production-ready Angular service named `{{SERVICE_NAME}}` that communicates with a REST API for the entity `{{ENTITY}}`.

**API base URL:** `{{API_BASE_URL}}` (e.g., `/api/v1/{{ENTITY_PLURAL}}`)
**ID type:** `{{ID_TYPE}}` (e.g., `number`, `string`)

Requirements:

- **`HttpClient`** injected via constructor (standalone inject pattern: `inject(HttpClient)`)
- **Full CRUD methods**, each returning an `Observable`:
  - `getAll(): Observable<{{ENTITY}}[]>`
  - `getById(id: {{ID_TYPE}}): Observable<{{ENTITY}}>`
  - `create(dto: Create{{ENTITY}}Dto): Observable<{{ENTITY}}>`
  - `update(id: {{ID_TYPE}}, dto: Update{{ENTITY}}Dto): Observable<{{ENTITY}}>`
  - `delete(id: {{ID_TYPE}}): Observable<void>`
- **Error handling** — pipe every request through a private `handleError()` method using `catchError` that:
  - Logs the error to console (dev only)
  - Re-throws a user-friendly `Error` with a readable message
- **TypeScript interfaces** — generate `{{ENTITY}}`, `Create{{ENTITY}}Dto`, and `Update{{ENTITY}}Dto` in the same file (or a separate `{{ENTITY_LOWER}}.model.ts` — note both options)
- Use `providedIn: 'root'` for the service decorator
- No `.subscribe()` inside the service — leave that to the component

Also generate:

1. **Unit test** (`{{SERVICE_NAME_LOWER}}.service.spec.ts`) using `HttpClientTestingModule` and `HttpTestingController`:
   - Test `getAll()` makes a GET request to the correct URL
   - Test `create()` makes a POST request with the correct body
   - Test `handleError()` re-throws on HTTP error (4xx/5xx)
   - Call `httpMock.verify()` in `afterEach`
2. **Usage example** — inject the service in a component, call `getAll()` with `AsyncPipe`, handle loading and error states

Output each file in a separate code block labeled with its filename.
