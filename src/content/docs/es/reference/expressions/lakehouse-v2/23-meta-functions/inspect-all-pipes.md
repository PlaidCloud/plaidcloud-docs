---
title: INSPECT_ALL_PIPES (Lakehouse v2)
description: INSPECT_ALL_PIPES — Devuelve información sobre todos los objetos de canalización (pipe).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-all-pipes.md
---

Devuelve información sobre todos los objetos de canalización (pipe).

## Sintaxis de Analyze

```python
func.inspect_all_pipes()
```

## Ejemplos de Analyze

```python
func.inspect_all_pipes()

┌─────────────┐
│ (pipe info)  │
└─────────────┘
```

## Sintaxis de SQL

```sql
INSPECT_ALL_PIPES()
```

## Ejemplos de SQL

```sql
SELECT * FROM TABLE(INSPECT_ALL_PIPES());

┌────────────────┐
│ (pipe details)  │
└────────────────┘
```
