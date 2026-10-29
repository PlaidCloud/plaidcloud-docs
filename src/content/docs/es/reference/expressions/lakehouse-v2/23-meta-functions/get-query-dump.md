---
title: GET_QUERY_DUMP (Lakehouse v2)
description: GET_QUERY_DUMP — Devuelve un volcado de consulta con fines de diagnóstico.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/get-query-dump.md
---

Devuelve un volcado de consulta con fines de diagnóstico.

## Sintaxis de Analyze

```python
func.get_query_dump(<query>)
```

## Ejemplos de Analyze

```python
func.get_query_dump('SELECT * FROM t')

┌────────┐
│ (dump)  │
└────────┘
```

## Sintaxis de SQL

```sql
GET_QUERY_DUMP(<query>)
```

## Ejemplos de SQL

```sql
SELECT GET_QUERY_DUMP('SELECT * FROM t');

┌───────────────────┐
│ (diagnostic dump)  │
└───────────────────┘
```
