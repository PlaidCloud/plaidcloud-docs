---
title: JSON_KEYS (Lakehouse v2)
description: JSON_KEYS — retorna as chaves do objeto JSON de nível superior como um array JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-keys.md
---

Retorna as chaves do objeto JSON de nível superior como um array JSON.

## Sintaxe do Analyze

```python
func.json_keys(get_column(table, 'data'))
```

## Exemplos do Analyze

```python
func.json_keys(get_column(table, 'data'))

┌────────────────┐
│ ["name","age"] │
└────────────────┘
```

## Sintaxe SQL

```sql
JSON_KEYS(<data>)
```

## Exemplos de SQL

```sql
SELECT JSON_KEYS(PARSE_JSON('{"name":"Alice","age":30}'));

┌────────────────┐
│ ["name","age"] │
└────────────────┘
```
