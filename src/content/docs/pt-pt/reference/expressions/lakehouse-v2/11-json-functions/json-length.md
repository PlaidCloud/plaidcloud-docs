---
title: JSON_LENGTH (Lakehouse v2)
description: JSON_LENGTH — devolve o número de elementos de um objeto ou matriz JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-length.md
---

Devolve o número de elementos de um objeto ou matriz JSON.

## Sintaxe de Analyze

```python
func.json_length(get_column(table, 'data'))
```

## Exemplos de Analyze

```python
func.json_length(get_column(table, 'data'))

┌───┐
│ 2 │
└───┘
```

## Sintaxe SQL

```sql
JSON_LENGTH(<data>)
```

## Exemplos SQL

```sql
SELECT JSON_LENGTH(PARSE_JSON('{"name":"Alice","age":30}'));

┌───┐
│ 2 │
└───┘
```
