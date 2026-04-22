# React Component Generator

**Model:** Claude Sonnet 4.6 / GPT-4o
**Category:** frontend
**Variables:** `{{COMPONENT_NAME}}`, `{{DESCRIPTION}}`, `{{PROPS}}`

---

Generate a production-ready React functional component named `{{COMPONENT_NAME}}`.

**Purpose:** `{{DESCRIPTION}}`

**Props interface:**
```
{{PROPS}}
```
(Example: `label: string`, `onClick: () => void`, `disabled?: boolean`)

Requirements:

- **TypeScript** — define a `{{COMPONENT_NAME}}Props` interface; no implicit `any`
- **Tailwind CSS** — use utility classes for all styling; use `clsx` or `cn()` for conditional classes
- **Accessibility** — include `aria-*` attributes where relevant (e.g., `aria-disabled`, `aria-label`); keyboard navigable
- **Named export** only — no default export
- **No side effects in render** — no direct DOM manipulation, no `console.log` left in code
- If the component handles async state, use `useState` + `useEffect` with proper cleanup
- If it receives a callback prop, wrap it in `useCallback`

Also generate:

1. **Unit test** (`{{COMPONENT_NAME}}.test.tsx`) using React Testing Library + Vitest:
   - Renders without crashing
   - Tests the primary interaction (click, input change, etc.)
   - Tests the disabled/error state if applicable
2. **Storybook story** (`{{COMPONENT_NAME}}.stories.tsx`) with:
   - Default story
   - At least one variant story (e.g., disabled, loading, error state)
3. **Usage example** — a 5-line snippet showing how to import and use the component

Output each file in a separate code block labeled with its filename.
