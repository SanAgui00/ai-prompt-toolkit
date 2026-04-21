# Spring Boot Startup Error Debugger

**Model:** Claude Sonnet 4.6 / GPT-4o
**Category:** debugging
**Variables:** `{{ERROR_LOG}}`, `{{APPLICATION_PROPERTIES}}`, `{{POM_SNIPPET}}`

---

A Spring Boot application fails to start. Diagnose the issue.

**Error log:**
```
{{ERROR_LOG}}
```

**application.properties / application.yml (relevant sections):**
```
{{APPLICATION_PROPERTIES}}
```

**pom.xml dependencies (if relevant):**
```xml
{{POM_SNIPPET}}
```

Diagnose and fix:
1. **Error class** — identify if this is: bean creation failure, datasource connection issue, port conflict, missing property, version incompatibility, or circular dependency
2. **Root cause** — the specific misconfiguration or missing piece
3. **Fix** — exact change needed in properties, pom.xml, or Java config
4. **Quick test** — how to verify the fix without full restart if possible (e.g., `curl /actuator/health`, check logs for specific line)
5. **Common Spring Boot startup errors reference** — list 3 other errors in the same class and their fixes, for future reference

If multiple errors are present, prioritize in order: datasource → bean wiring → missing config → version conflicts.
