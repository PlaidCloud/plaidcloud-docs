---
title: IS_FLOAT (Lakehouse v1)
description: IS_FLOAT — Verifica se o valor JSON de entrada é um float.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-float.md
---

Verifica se o valor JSON de entrada é um float.

## Sintaxe do Analyze

```python
func.is_float(<expr>)
```

## Exemplos do Analyze

```python

func.is_float(func.parse_json('1.23')), func.is_float(func.parse_json('[1,2,3]'))
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_float(func.parse_json('1.23'))   │ func.is_float(func.parse_json('[1,2,3]'))   │
├──────────────────────────────────────────┼─────────────────────────────────────────────┤
│ true                                     │ false                                       │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
IS_FLOAT( <expr> )
```

## Tipo de retorno

Retorna `true` se o valor JSON de entrada for um float e `false` caso contrário.

## Exemplos de SQL

```sql
SELECT
  IS_FLOAT(PARSE_JSON('1.23')),
  IS_FLOAT(PARSE_JSON('[1,2,3]'));

┌────────────────────────────────────────────────────────────────┐
│ is_float(parse_json('1.23')) │ is_float(parse_json('[1,2,3]')) │
├──────────────────────────────┼─────────────────────────────────┤
│ true                         │ false                           │
└────────────────────────────────────────────────────────────────┘
```
