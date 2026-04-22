# SQL Query Code Review

**Model:** Claude Sonnet 4.6 / GPT-4o
**Category:** code-review
**Variables:** `{{SQL_CODE}}`, `{{DB_ENGINE}}`, `{{TABLE_SCHEMA}}`

---

Review the following SQL query for a `{{DB_ENGINE}}` database:

```sql
{{SQL_CODE}}
```

Relevant table schema:
```sql
{{TABLE_SCHEMA}}
```

Evaluate across these axes:

1. **Correctness**
   - Query returns the intended result set (check JOINs, WHERE conditions, GROUP BY, HAVING)
   - Correct handling of NULLs (use `IS NULL` not `= NULL`, beware of outer join NULLs in aggregations)
   - No off-by-one in LIMIT/OFFSET pagination

2. **Performance**
   - Identify missing indexes on columns used in WHERE, JOIN ON, and ORDER BY
   - Flag full table scans (`SELECT *`, functions on indexed columns, implicit type casts)
   - Suggest query rewrites: EXISTS vs IN, covering indexes, partitioning hints
   - Estimate relative cost if obvious (e.g., "this scans ~10M rows without an index on `created_at`")

3. **Security**
   - Flag any string concatenation that indicates SQL injection risk
   - Confirm parameterized queries / prepared statements are used
   - Check for overly permissive data exposure (SELECT * returning sensitive columns)

4. **Readability**
   - Consistent capitalization of SQL keywords
   - Aliases are meaningful, not single letters
   - Complex logic broken into CTEs instead of deeply nested subqueries

5. **Maintainability**
   - No hardcoded magic values (use named parameters or constants)
   - Query is idempotent where it should be (INSERT ... ON DUPLICATE KEY / UPSERT)

**Output format:**
- Summary table: axis → Severity (OK / WARN / FAIL) + one-line finding
- Detailed findings with the problematic SQL snippet and a corrected version
- Recommended indexes to add (as `CREATE INDEX` statements)
- Overall verdict: APPROVE / REQUEST CHANGES + top 3 action items
