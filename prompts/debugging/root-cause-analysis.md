# Root Cause Analysis — Stack Trace Interpreter

**Model:** Claude Sonnet 4.6 / GPT-4o
**Category:** debugging
**Variables:** `{{STACK_TRACE}}`, `{{LANGUAGE}}`, `{{CONTEXT}}`

---

Analyze the following `{{LANGUAGE}}` stack trace and identify the root cause.

```
{{STACK_TRACE}}
```

Context about the system: `{{CONTEXT}}`

Provide:
1. **Root cause** — the actual line and reason the error originated (not just where it surfaced)
2. **Why it happened** — explain the chain of events leading to this error in plain terms
3. **Immediate fix** — minimal code change to resolve it, with a before/after snippet
4. **Proper fix** — the correct long-term solution if the immediate fix is a workaround
5. **How to prevent it** — one defensive coding pattern or validation that would catch this earlier

Keep the explanation concise. If the stack trace is ambiguous, state your assumptions explicitly before analyzing.
