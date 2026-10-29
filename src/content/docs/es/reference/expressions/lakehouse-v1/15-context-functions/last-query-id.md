---
title: LAST_QUERY_ID (Lakehouse v1)
description: LAST_QUERY_ID devuelve el ID de la última consulta de la sesión actual; el índice puede ser (-1, 1, 1+2).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/last-query-id.md
---

Devuelve el ID de la última consulta de la sesión actual; el índice puede ser (-1, 1, 1+2)... Un índice fuera de rango devuelve una cadena vacía.

## Sintaxis de Analyze

```python
func.last_query_id(<index>)
```

## Ejemplos de Analyze

```python
func.last_query_id(-1)

┌──────────────────────────────────────┐
│    func.last_query_id((- 1))         │
├──────────────────────────────────────┤
│ a6f615c6-5bad-4863-8558-afd01889448c │
└──────────────────────────────────────┘
```


## Sintaxis de SQL

```sql
LAST_QUERY_ID(<index>)
```

## Ejemplos de SQL

```sql
SELECT LAST_QUERY_ID(-1);

┌──────────────────────────────────────┐
│         last_query_id((- 1))         │
├──────────────────────────────────────┤
│ a6f615c6-5bad-4863-8558-afd01889448c │
└──────────────────────────────────────┘
```
