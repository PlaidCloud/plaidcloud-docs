---
title: IS_FLOAT (Lakehouse v1)
description: IS_FLOAT — sprawdza, czy wejściowa wartość JSON jest liczbą zmiennoprzecinkową.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-float.md
---

Sprawdza, czy wejściowa wartość JSON jest liczbą zmiennoprzecinkową.

## Składnia Analyze

```python
func.is_float(<expr>)
```

## Przykłady Analyze

```python

func.is_float(func.parse_json('1.23')), func.is_float(func.parse_json('[1,2,3]'))
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_float(func.parse_json('1.23'))   │ func.is_float(func.parse_json('[1,2,3]'))   │
├──────────────────────────────────────────┼─────────────────────────────────────────────┤
│ true                                     │ false                                       │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
IS_FLOAT( <expr> )
```

## Typ zwracany

Zwraca `true`, jeśli wejściowa wartość JSON jest liczbą zmiennoprzecinkową, a w przeciwnym razie `false`.

## Przykłady SQL

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
