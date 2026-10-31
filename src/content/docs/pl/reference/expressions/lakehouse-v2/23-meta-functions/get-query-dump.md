---
title: GET_QUERY_DUMP (Lakehouse v2)
description: GET_QUERY_DUMP — zwraca zrzut zapytania do celów diagnostycznych.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/get-query-dump.md
---

Zwraca zrzut zapytania do celów diagnostycznych.

## Składnia Analyze

```python
func.get_query_dump(<query>)
```

## Przykłady Analyze

```python
func.get_query_dump('SELECT * FROM t')

┌────────┐
│ (dump)  │
└────────┘
```

## Składnia SQL

```sql
GET_QUERY_DUMP(<query>)
```

## Przykłady SQL

```sql
SELECT GET_QUERY_DUMP('SELECT * FROM t');

┌───────────────────┐
│ (diagnostic dump)  │
└───────────────────┘
```
