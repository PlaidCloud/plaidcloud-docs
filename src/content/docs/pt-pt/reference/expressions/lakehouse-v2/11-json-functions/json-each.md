---
title: JSON_EACH (Lakehouse v2)
description: JSON_EACH — expande o objeto JSON de nível superior num conjunto de pares chave-valor.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-each.md
---

Expande o objeto JSON de nível superior num conjunto de pares chave-valor.

## Sintaxe de Analyze

```python
func.json_each(get_column(table, 'data'))
```

## Exemplos de Analyze

```python
func.json_each(get_column(table, 'data'))
```

## Sintaxe SQL

```sql
JSON_EACH(<data>)
```

## Exemplos SQL

```sql
SELECT * FROM TABLE(JSON_EACH(PARSE_JSON('{"a":1,"b":2}')));

┌─────┬───────┐
│ key │ value │
├─────┼───────┤
│ a   │ 1     │
│ b   │ 2     │
└─────┴───────┘
```
