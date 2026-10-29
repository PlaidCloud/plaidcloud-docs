---
title: GET_QUERY_DUMP (Lakehouse v2)
description: GET_QUERY_DUMP — renvoie un dump de requête à des fins de diagnostic.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/get-query-dump.md
---

Renvoie un dump de requête à des fins de diagnostic.

## Syntaxe Analyze

```python
func.get_query_dump(<query>)
```

## Exemples Analyze

```python
func.get_query_dump('SELECT * FROM t')

┌────────┐
│ (dump)  │
└────────┘
```

## Syntaxe SQL

```sql
GET_QUERY_DUMP(<query>)
```

## Exemples SQL

```sql
SELECT GET_QUERY_DUMP('SELECT * FROM t');

┌───────────────────┐
│ (diagnostic dump)  │
└───────────────────┘
```
