---
title: JSON_LENGTH (Lakehouse v2)
description: JSON_LENGTH — retorna o número de elementos em um objeto ou array JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-length.md
---

Retorna o número de elementos em um objeto ou array JSON.

## Sintaxe do Analyze

```python
func.json_length(get_column(table, 'data'))
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT JSON_LENGTH(PARSE_JSON('{"name":"Alice","age":30}'));

┌───┐
│ 2 │
└───┘
```
