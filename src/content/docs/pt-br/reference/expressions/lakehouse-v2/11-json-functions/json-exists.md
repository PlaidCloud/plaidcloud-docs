---
title: JSON_EXISTS (Lakehouse v2)
description: JSON_EXISTS — verifica se um documento JSON contém um valor em um caminho especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-exists.md
---

Verifica se um documento JSON contém um valor em um caminho especificado.

## Sintaxe do Analyze

```python
func.json_exists(get_column(table, 'data'), '$.name')
```

## Exemplos do Analyze

```python
func.json_exists(get_column(table, 'data'), '$.name')

┌───┐
│ 1 │
└───┘
```

## Sintaxe SQL

```sql
JSON_EXISTS(<data>, '$.name')
```

## Exemplos de SQL

```sql
SELECT JSON_EXISTS(PARSE_JSON('{"name":"Alice"}'), '$.name');

┌───┐
│ 1 │
└───┘
```
