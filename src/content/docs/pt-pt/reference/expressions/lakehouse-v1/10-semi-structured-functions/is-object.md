---
title: IS_OBJECT (Lakehouse v1)
description: IS_OBJECT — Verifica se o valor de entrada é um objeto JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-object.md
---

Verifica se o valor de entrada é um objeto JSON.

## Sintaxe do Analyze

```python
func.is_object(<expr>)
```

## Exemplos do Analyze

```python

func.is_object(func.parse_json('{"a":"b"}')), func.is_object(func.parse_json('["a","b","c"]'))
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_object(func.parse_json('{"a":"b"}'))  │ func.is_object(func.parse_json('["a","b","c"]')) │
├───────────────────────────────────────────────┼──────────────────────────────────────────────────┤
│ true                                          │ false                                            │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
IS_OBJECT( <expr> )
```

## Tipo de retorno

Devolve `true` se o valor JSON de entrada for um objeto JSON e `false` caso contrário.

## Exemplos de SQL

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
