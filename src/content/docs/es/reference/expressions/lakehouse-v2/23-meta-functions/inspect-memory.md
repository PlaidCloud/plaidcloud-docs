---
title: INSPECT_MEMORY (Lakehouse v2)
description: INSPECT_MEMORY — Devuelve información sobre el uso de memoria del nodo actual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-memory.md
---

Devuelve información sobre el uso de memoria del nodo actual.

## Sintaxis de Analyze

```python
func.inspect_memory()
```

## Ejemplos de Analyze

```python
func.inspect_memory()

┌───────────────┐
│ (memory info)  │
└───────────────┘
```

## Sintaxis de SQL

```sql
INSPECT_MEMORY()
```

## Ejemplos de SQL

```sql
SELECT * FROM TABLE(INSPECT_MEMORY());

┌──────────────────┐
│ (memory details)  │
└──────────────────┘
```
