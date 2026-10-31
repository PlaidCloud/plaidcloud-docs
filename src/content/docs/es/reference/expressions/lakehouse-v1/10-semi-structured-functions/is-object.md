---
title: IS_OBJECT (Lakehouse v1)
description: IS_OBJECT — Comprueba si el valor de entrada es un objeto JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-object.md
---

Comprueba si el valor de entrada es un objeto JSON.

## Sintaxis de Analyze

```python
func.is_object(<expr>)
```

## Ejemplos de Analyze

```python

func.is_object(func.parse_json('{"a":"b"}')), func.is_object(func.parse_json('["a","b","c"]'))
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_object(func.parse_json('{"a":"b"}'))  │ func.is_object(func.parse_json('["a","b","c"]')) │
├───────────────────────────────────────────────┼──────────────────────────────────────────────────┤
│ true                                          │ false                                            │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
IS_OBJECT( <expr> )
```

## Tipo de retorno

Devuelve `true` si el valor JSON de entrada es un objeto JSON y `false` en caso contrario.

## Ejemplos de SQL

```sql
SELECT
  IS_OBJECT(PARSE_JSON('{"a":"b"}')), -- JSON Object
  IS_OBJECT(PARSE_JSON('["a","b","c"]')); --JSON Array

┌─────────────────────────────────────────────────────────────────────────────┐
│ is_object(parse_json('{"a":"b"}')) │ is_object(parse_json('["a","b","c"]')) │
├────────────────────────────────────┼────────────────────────────────────────┤
│ true                               │ false                                  │
└─────────────────────────────────────────────────────────────────────────────┘
```
