---
title: INSPECT_MEMORY_DETAIL (Lakehouse v2)
description: INSPECT_MEMORY_DETAIL — Devuelve información detallada sobre el uso de memoria.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-memory-detail.md
---

Devuelve información detallada sobre el uso de memoria.

## Sintaxis de Analyze

```python
func.inspect_memory_detail()
```

## Ejemplos de Analyze

```python
func.inspect_memory_detail()

┌──────────┐
│ (detail)  │
└──────────┘
```

## Sintaxis de SQL

```sql
INSPECT_MEMORY_DETAIL()
```

## Ejemplos de SQL

```sql
SELECT * FROM TABLE(INSPECT_MEMORY_DETAIL());

┌─────────────────┐
│ (memory detail)  │
└─────────────────┘
```
