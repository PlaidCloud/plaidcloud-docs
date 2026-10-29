---
title: INSPECT_ALL_PIPES (Lakehouse v2)
description: INSPECT_ALL_PIPES — gibt Informationen zu allen Pipe-Objekten zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-all-pipes.md
---

Gibt Informationen zu allen Pipe-Objekten zurück.

## Analyze-Syntax

```python
func.inspect_all_pipes()
```

## Analyze-Beispiele

```python
func.inspect_all_pipes()

┌─────────────┐
│ (pipe info)  │
└─────────────┘
```

## SQL-Syntax

```sql
INSPECT_ALL_PIPES()
```

## SQL-Beispiele

```sql
SELECT * FROM TABLE(INSPECT_ALL_PIPES());

┌────────────────┐
│ (pipe details)  │
└────────────────┘
```
