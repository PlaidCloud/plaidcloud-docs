---
title: JSON_STRIP_NULLS (Lakehouse v1)
description: JSON_STRIP_NULLS — elimina de un objeto JSON todas las propiedades con valores nulos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-strip-nulls.md
---

Elimina de un objeto JSON todas las propiedades con valores nulos. 

## Sintaxis de Analyze

```python
func.json_strip_nulls(<json_string>)
```

## Ejemplos de Analyze

```python
func.json_strip_nulls(func.parse_json('{"name": "alice", "age": 30, "city": null}'))

┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.json_strip_nulls(func.parse_json('{"name": "alice", "age": 30, "city": null}'))            │
│                                         String                                                  │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ {"age":30,"name":"Alice"}                                                                       │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
JSON_STRIP_NULLS(<json_string>)
```

## Tipo de retorno

Devuelve un valor del mismo tipo que el valor JSON de entrada.

## Ejemplos de SQL

```sql
SELECT JSON_STRIP_NULLS(PARSE_JSON('{"name": "Alice", "age": 30, "city": null}'));

json_strip_nulls(parse_json('{"name": "alice", "age": 30, "city": null}'))|
--------------------------------------------------------------------------+
{"age":30,"name":"Alice"}                                                 |
```
