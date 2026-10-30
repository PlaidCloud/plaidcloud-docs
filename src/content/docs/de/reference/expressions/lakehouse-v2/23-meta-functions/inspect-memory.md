---
title: INSPECT_MEMORY (Lakehouse v2)
description: INSPECT_MEMORY — Gibt Informationen zur Speichernutzung des aktuellen Knotens zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-memory.md
---

Gibt Informationen zur Speichernutzung des aktuellen Knotens zurück.

## Analyze-Syntax

```python
func.inspect_memory()
```

## Analyze-Beispiele

```python
func.inspect_memory()

┌───────────────┐
│ (memory info)  │
└───────────────┘
```

## SQL-Syntax

```sql
INSPECT_MEMORY()
```

## SQL-Beispiele

```sql
SELECT * FROM TABLE(INSPECT_MEMORY());

┌──────────────────┐
│ (memory details)  │
└──────────────────┘
```
