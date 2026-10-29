---
title: IS_STRING (Lakehouse v1)
description: IS_STRING — Verifica se o valor JSON de entrada é uma cadeia.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-string.md
---

Verifica se o valor JSON de entrada é uma cadeia.

## Sintaxe do Analyze

```python
func.is_string(<expr>)
```

## Exemplos do Analyze

```python

func.is_string(func.parse_json('"abc"')), func.is_string(func.parse_json('123'))
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_string(func.parse_json('"abc"'))      │ func.is_string(func.parse_json('123'))           │
├───────────────────────────────────────────────┼──────────────────────────────────────────────────┤
│ true                                          │ false                                            │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
IS_STRING( <expr> )
```

## Tipo de retorno

Devolve `true` se o valor JSON de entrada for uma cadeia e `false` caso contrário.

## Exemplos de SQL

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
