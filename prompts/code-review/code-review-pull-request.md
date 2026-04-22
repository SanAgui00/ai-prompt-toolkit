# General Pull Request Code Review

**Model:** Claude Sonnet 4.6 / GPT-4o
**Category:** code-review
**Variables:** `{{PR_DIFF}}`, `{{PR_DESCRIPTION}}`, `{{TECH_STACK}}`

---

Review the following pull request for a `{{TECH_STACK}}` project.

**PR Description:**
```
{{PR_DESCRIPTION}}
```

**Diff:**
```diff
{{PR_DIFF}}
```

Conduct a thorough review across five axes:

1. **Correctness**
   - Does the code do what the PR description claims?
   - Are edge cases handled (empty collections, null inputs, concurrent access)?
   - Are error paths tested, not just the happy path?

2. **Security**
   - Any new attack surface: unvalidated input, insecure deserialization, path traversal, open redirects?
   - Secrets or credentials accidentally included in the diff?
   - Dependencies added — flag if any have known CVEs or are unmaintained

3. **Readability**
   - Names (variables, functions, classes) communicate intent clearly
   - Functions do one thing; no method longer than ~30 lines without strong justification
   - Comments explain *why*, not *what*

4. **Architecture**
   - Does the change respect existing layer boundaries (controller → service → repository)?
   - No circular dependencies introduced
   - New abstractions justified — not premature generalization for a one-off case

5. **Performance**
   - No O(n²) loops introduced on unbounded collections
   - Database queries inside loops (N+1 problem)?
   - Large payloads loaded fully into memory when streaming would suffice?

**Checklist before APPROVE:**
- [ ] Tests added or updated for every changed behavior
- [ ] No new compiler warnings or linting errors
- [ ] Documentation updated if public API changed
- [ ] Migration script included if schema changed
- [ ] Feature flag or rollback plan documented for risky changes

**Output format:**
- Summary table: axis → Severity (OK / WARN / FAIL) + one-line finding
- Inline comments: quote the specific line(s) + severity + explanation + suggested fix
- Final verdict: APPROVE / APPROVE WITH NITS / REQUEST CHANGES + top 3 blocking issues (if any)
