# JPA Repository + Service Layer Generator

**Model:** Claude Sonnet 4.6 / GPT-4o
**Category:** backend
**Variables:** `{{ENTITY}}`, `{{PACKAGE}}`, `{{ID_TYPE}}`, `{{DB_TABLE}}`

---

Generate a complete JPA persistence layer for `{{ENTITY}}` in package `{{PACKAGE}}`.

**1. Entity class** (`{{ENTITY}}.java`):
- `@Entity`, `@Table(name = "{{DB_TABLE}}")`
- `@Id` with `@GeneratedValue(strategy = GenerationType.IDENTITY)` for `{{ID_TYPE}}`
- Include `createdAt` and `updatedAt` with `@CreationTimestamp` / `@UpdateTimestamp`
- Use Lombok: `@Getter`, `@Setter`, `@NoArgsConstructor`, `@AllArgsConstructor`, `@Builder`
- Add index annotations on commonly queried fields if applicable

**2. Repository interface** (`{{ENTITY}}Repository.java`):
- Extend `JpaRepository<{{ENTITY}}, {{ID_TYPE}}>`
- Add 2-3 derived query methods relevant to the entity (e.g., findByStatus, findByCreatedAtBetween)
- Add one `@Query` JPQL example with pagination support

**3. Service implementation** (`{{ENTITY}}ServiceImpl.java`):
- Implement full CRUD: findAll (paginated), findById, create, update, delete
- Throw `ResourceNotFoundException` (custom) on missing entity
- Map between entity and DTO using a private helper method (no MapStruct, keep it simple)
- Use `@Transactional` on write methods
- Use `@Slf4j` for logging key operations

**4. Custom exception** (`ResourceNotFoundException.java`):
- Extend `RuntimeException`
- Constructor accepting resource name and field value

Output each class in a separate labeled code block.
