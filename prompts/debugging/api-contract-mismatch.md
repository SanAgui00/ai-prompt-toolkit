# API Contract Mismatch Debugger

**Model:** Claude Sonnet 4.6 / GPT-4o
**Category:** debugging
**Variables:** `{{EXPECTED_REQUEST}}`, `{{ACTUAL_REQUEST}}`, `{{RESPONSE}}`, `{{ENDPOINT}}`

---

A REST API call to `{{ENDPOINT}}` is not behaving as expected.

**What the client is sending:**
```json
{{ACTUAL_REQUEST}}
```

**What the API expects (contract / DTO):**
```json
{{EXPECTED_REQUEST}}
```

**Response received:**
```
{{RESPONSE}}
```

Diagnose the mismatch and provide:
1. **What's wrong** — field names, types, nesting, or missing required fields
2. **Corrected request** — the exact JSON the client should send
3. **Server-side fix** (if applicable) — if the API contract itself is the problem, show the DTO or validation change
4. **Checklist** — common causes to rule out: serialization config, `@JsonProperty` mismatches, null vs missing fields, case sensitivity, date format
