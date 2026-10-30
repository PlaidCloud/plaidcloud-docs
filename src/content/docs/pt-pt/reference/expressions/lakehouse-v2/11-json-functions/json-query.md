---
title: JSON_QUERY (Lakehouse v2)
description: JSON_QUERY — extrai um valor JSON de um documento JSON através de uma expressão de caminho.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-query.md
---

Extrai um valor JSON de um documento JSON através de uma expressão de caminho.

## Sintaxe de Analyze

```python
func.json_query(get_column(table, 'data'), '$.items')
```

## Exemplos de Analyze

```python
func.json_query(get_column(table, 'data'), '$.items')

┌────────────┐
│ JSON value │
└────────────┘
```

## Sintaxe SQL

```sql
JSON_QUERY(<data>, '$.items')
```

## Exemplos SQL

```sql
SELECT JSON_QUERY(PARSE_JSON('{"items":[1,2,3]}'), '$.items');

┌─────────┐
│ [1,2,3] │
└─────────┘
```
