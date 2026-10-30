---
title: JSON_STRIP_NULLS (Lakehouse v1)
description: JSON_STRIP_NULLS — remove todas as propriedades com valores nulos de um objeto JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-strip-nulls.md
---

Remove todas as propriedades com valores nulos de um objeto JSON. 

## Sintaxe do Analyze

```python
func.json_strip_nulls(<json_string>)
```

## Exemplos do Analyze

```python
func.json_strip_nulls(func.parse_json('{"name": "alice", "age": 30, "city": null}'))

┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.json_strip_nulls(func.parse_json('{"name": "alice", "age": 30, "city": null}'))            │
│                                         String                                                  │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ {"age":30,"name":"Alice"}                                                                       │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
JSON_STRIP_NULLS(<json_string>)
```

## Tipo de retorno

Devolve um valor do mesmo tipo que o valor JSON de entrada.

## Exemplos de SQL

```sql
SELECT JSON_STRIP_NULLS(PARSE_JSON('{"name": "Alice", "age": 30, "city": null}'));

json_strip_nulls(parse_json('{"name": "alice", "age": 30, "city": null}'))|
--------------------------------------------------------------------------+
{"age":30,"name":"Alice"}                                                 |
```
