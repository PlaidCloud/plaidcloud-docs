---
title: LAST_QUERY_ID (Lakehouse v2)
description: LAST_QUERY_ID — Gibt die ID der zuletzt ausgeführten Abfrage zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/last-query-id.md
---

Gibt die ID der zuletzt ausgeführten Abfrage zurück.

## Analyze-Syntax

```python
func.last_query_id()
```

## Analyze-Beispiele

```python
func.last_query_id()

┌───────────────┐
│ 'abc-123-def'  │
└───────────────┘
```

## SQL-Syntax

```sql
LAST_QUERY_ID()
```

## SQL-Beispiele

```sql
SELECT LAST_QUERY_ID();

┌─────────────────┐
│ abc-123-def-456  │
└─────────────────┘
```
