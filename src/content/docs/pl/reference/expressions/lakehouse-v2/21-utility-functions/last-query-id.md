---
title: LAST_QUERY_ID (Lakehouse v2)
description: LAST_QUERY_ID — zwraca identyfikator ostatnio wykonanego zapytania.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/last-query-id.md
---

Zwraca identyfikator ostatnio wykonanego zapytania.

## Składnia Analyze

```python
func.last_query_id()
```

## Przykłady Analyze

```python
func.last_query_id()

┌───────────────┐
│ 'abc-123-def'  │
└───────────────┘
```

## Składnia SQL

```sql
LAST_QUERY_ID()
```

## Przykłady SQL

```sql
SELECT LAST_QUERY_ID();

┌─────────────────┐
│ abc-123-def-456  │
└─────────────────┘
```
