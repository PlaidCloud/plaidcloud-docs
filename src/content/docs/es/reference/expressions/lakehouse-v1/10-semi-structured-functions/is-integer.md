---
title: IS_INTEGER (Lakehouse v1)
description: IS_INTEGER — Comprueba si el valor JSON de entrada es un entero.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-integer.md
---

Comprueba si el valor JSON de entrada es un entero.


## Sintaxis de Analyze

```python
func.is_integer(<expr>)
```

## Ejemplos de Analyze

```python

func.is_integer(func.parse_json('123')), func.is_integer(func.parse_json('[1,2,3]'))
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_integer(func.parse_json('123'))  │ func.is_integer(func.parse_json('[1,2,3]')) │
├──────────────────────────────────────────┼─────────────────────────────────────────────┤
│ true                                     │ false                                       │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
IS_INTEGER( <expr> )
```

## Tipo de retorno

Devuelve `true` si el valor JSON de entrada es un entero y `false` en caso contrario.

## Ejemplos de SQL

```sql
SELECT
  IS_INTEGER(PARSE_JSON('123')),
  IS_INTEGER(PARSE_JSON('[1,2,3]'));

┌───────────────────────────────────────────────────────────────────┐
│ is_integer(parse_json('123')) │ is_integer(parse_json('[1,2,3]')) │
├───────────────────────────────┼───────────────────────────────────┤
│ true                          │ false                             │
└───────────────────────────────────────────────────────────────────┘
```
