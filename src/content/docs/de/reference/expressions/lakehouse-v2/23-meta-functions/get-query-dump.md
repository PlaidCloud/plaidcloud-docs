---
title: GET_QUERY_DUMP (Lakehouse v2)
description: GET_QUERY_DUMP — gibt einen Abfrage-Dump zu Diagnosezwecken zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/get-query-dump.md
---

Gibt einen Abfrage-Dump zu Diagnosezwecken zurück.

## Analyze-Syntax

```python
func.get_query_dump(<query>)
```

## Analyze-Beispiele

```python
func.get_query_dump('SELECT * FROM t')

┌────────┐
│ (dump)  │
└────────┘
```

## SQL-Syntax

```sql
GET_QUERY_DUMP(<query>)
```

## SQL-Beispiele

```sql
SELECT GET_QUERY_DUMP('SELECT * FROM t');

┌───────────────────┐
│ (diagnostic dump)  │
└───────────────────┘
```
