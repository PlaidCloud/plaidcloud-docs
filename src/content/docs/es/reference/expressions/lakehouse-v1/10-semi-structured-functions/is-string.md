---
title: IS_STRING (Lakehouse v1)
description: IS_STRING — Comprueba si el valor JSON de entrada es una cadena.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-string.md
---

Comprueba si el valor JSON de entrada es una cadena.

## Sintaxis de Analyze

```python
func.is_string(<expr>)
```

## Ejemplos de Analyze

```python

func.is_string(func.parse_json('"abc"')), func.is_string(func.parse_json('123'))
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_string(func.parse_json('"abc"'))      │ func.is_string(func.parse_json('123'))           │
├───────────────────────────────────────────────┼──────────────────────────────────────────────────┤
│ true                                          │ false                                            │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
IS_STRING( <expr> )
```

## Tipo de retorno

Devuelve `true` si el valor JSON de entrada es una cadena y `false` en caso contrario.

## Ejemplos de SQL

```sql
SELECT
  IS_STRING(PARSE_JSON('"abc"')),
  IS_STRING(PARSE_JSON('123'));

┌───────────────────────────────────────────────────────────────┐
│ is_string(parse_json('"abc"')) │ is_string(parse_json('123')) │
├────────────────────────────────┼──────────────────────────────┤
│ true                           │ false                        │
└───────────────────────────────────────────────────────────────┘
```
