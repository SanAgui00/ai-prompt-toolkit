# SQL Query Debugger + Optimizer

**Model:** Claude Sonnet 4.6 / GPT-4o
**Category:** debugging
**Variables:** `{{SQL_QUERY}}`, `{{SCHEMA}}`, `{{ERROR_OR_SYMPTOM}}`, `{{DB_ENGINE}}`

---

Debug and optimize the following `{{DB_ENGINE}}` query.

**Query:**
```sql
{{SQL_QUERY}}
```

**Schema (relevant tables):**
```sql
{{SCHEMA}}
```

**Problem:** `{{ERROR_OR_SYMPTOM}}`

Provide:
1. **Diagnosis** — what is wrong or inefficient and why
2. **Fixed query** — corrected version with explanation of each change
3. **Performance analysis** — identify missing indexes, full table scans, or N+1 patterns if present
4. **Suggested indexes** — `CREATE INDEX` statements if they would help, with justification
5. **EXPLAIN output interpretation** — if an EXPLAIN plan is provided, interpret the key rows

If the query is correct but slow, focus entirely on optimization.
If the query has a logic error, fix correctness first, then optimize.
