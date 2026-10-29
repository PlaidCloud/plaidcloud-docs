---
title: IS_BOOLEAN (Lakehouse v1)
description: IS_BOOLEAN — Verifica se o valor JSON de entrada é um booleano.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-boolean.md
---

Verifica se o valor JSON de entrada é um booleano.

## Sintaxe do Analyze

```python
func.is_boolean(<expr>)
```

## Exemplos do Analyze

```python

func.is_boolean(func.parse_json('true')), func.is_boolean(func.parse_json('[1,2,3]'))
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_boolean(func.parse_json('true')) │ func.is_boolean(func.parse_json('[1,2,3]')) │
├──────────────────────────────────────────┼─────────────────────────────────────────────┤
│ true                                     │ false                                       │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
IS_BOOLEAN( <expr> )
```

## Tipo de retorno

Devolve `true` se o valor JSON de entrada for um booleano e `false` caso contrário.

## Exemplos de SQL

```sql
SELECT
  IS_BOOLEAN(PARSE_JSON('true')),
  IS_BOOLEAN(PARSE_JSON('[1,2,3]'));

┌────────────────────────────────────────────────────────────────────┐
│ is_boolean(parse_json('true')) │ is_boolean(parse_json('[1,2,3]')) │
├────────────────────────────────┼───────────────────────────────────┤
│ true                           │ false                             │
└────────────────────────────────────────────────────────────────────┘
```
