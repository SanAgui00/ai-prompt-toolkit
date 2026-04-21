# AI Prompt Toolkit

A curated library of 20-30 production-tested prompts for accelerating software development workflows with Claude and GPT-4.

## Purpose

Reusable, parameterized prompts that reduce context-switching and increase consistency across dev tasks — from code generation to infrastructure review.

## Structure

```
prompts/
├── backend/        # API design, CRUD generation, Spring Boot, Laravel
├── frontend/       # Angular components, TypeScript, UI patterns
├── devops/         # Dockerfile, CI/CD, Terraform, AWS
├── debugging/      # Root cause analysis, error interpretation
└── code-review/    # Quality gates, security, performance

templates/          # Prompt templates with variable placeholders
examples/           # Before/after examples showing prompt output
scripts/            # Python utilities for prompt management
```

## Usage

Each prompt file follows the format:

```
# [Prompt Name]
**Model:** Claude 3.5 / GPT-4
**Category:** backend | frontend | devops | debugging | code-review
**Variables:** list of {{PLACEHOLDERS}}

---
[Prompt body]
```

## Metrics

- 20-30 reusable prompts across 5 categories
- Tested against Claude Sonnet and GPT-4o
- Average time saved: ~15-30 min per task

## Tech

- Python scripts for prompt validation and rendering
- Markdown-first documentation
- Compatible with Claude Code, Cursor, GitHub Copilot chat

## Status

Active development — Week 1-3 of 10-week portfolio sprint.
