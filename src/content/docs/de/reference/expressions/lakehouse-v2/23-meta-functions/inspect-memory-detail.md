---
title: INSPECT_MEMORY_DETAIL (Lakehouse v2)
description: INSPECT_MEMORY_DETAIL — Gibt detaillierte Informationen zur Speichernutzung zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-memory-detail.md
---

Gibt detaillierte Informationen zur Speichernutzung zurück.

## Analyze-Syntax

```python
func.inspect_memory_detail()
```

## Analyze-Beispiele

```python
func.inspect_memory_detail()

┌──────────┐
│ (detail)  │
└──────────┘
```

## SQL-Syntax

```sql
INSPECT_MEMORY_DETAIL()
```

## SQL-Beispiele

```sql
SELECT * FROM TABLE(INSPECT_MEMORY_DETAIL());

┌─────────────────┐
│ (memory detail)  │
└─────────────────┘
```
