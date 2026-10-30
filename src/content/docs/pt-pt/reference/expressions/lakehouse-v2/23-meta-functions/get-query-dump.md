---
title: GET_QUERY_DUMP (Lakehouse v2)
description: GET_QUERY_DUMP — devolve um dump de consulta para fins de diagnóstico.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/get-query-dump.md
---

Devolve um dump de consulta para fins de diagnóstico.

## Sintaxe do Analyze

```python
func.get_query_dump(<query>)
```

## Exemplos do Analyze

```python
func.get_query_dump('SELECT * FROM t')

┌────────┐
│ (dump)  │
└────────┘
```

## Sintaxe SQL

```sql
GET_QUERY_DUMP(<query>)
```

## Exemplos SQL

```sql
SELECT GET_QUERY_DUMP('SELECT * FROM t');

┌───────────────────┐
│ (diagnostic dump)  │
└───────────────────┘
```
