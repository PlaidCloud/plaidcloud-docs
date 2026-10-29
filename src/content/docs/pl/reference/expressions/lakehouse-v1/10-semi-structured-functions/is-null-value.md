---
title: IS_NULL_VALUE (Lakehouse v1)
description: IS_NULL_VALUE — sprawdza, czy wartość wejściowa jest wartością null w formacie JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-null-value.md
---

Sprawdza, czy wartość wejściowa jest wartością `null` w formacie JSON. Uwaga: ta funkcja bada wartość `null` w JSON, a nie wartość NULL w SQL. Aby sprawdzić, czy wartość jest wartością NULL w SQL, użyj funkcji [IS_NULL](../../03-conditional-functions/is-null).

```json title='JSON null Example:'
{
  "name": "John",
  "age": null
}   
```

## Składnia Analyze

```python
func.is_null_value(<expr>)
```

## Przykłady Analyze

```python

func.is_null_value(func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k5'))
┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_null_value(func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k5')) │
├─────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ true                                                                                                │
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
IS_NULL_VALUE( <expr> )
```

## Typ zwracany

Zwraca `true`, jeśli wartość wejściowa jest wartością `null` w formacie JSON, a w przeciwnym razie `false`.

## Przykłady SQL

```sql
SELECT
  IS_NULL_VALUE(PARSE_JSON('{"name":"John", "age":null}') :age), --JSON null
  IS_NULL(NULL); --SQL NULL

┌──────────────────────────────────────────────────────────────────────────────┐
│ is_null_value(parse_json('{"name":"john", "age":null}'):age) │ is_null(null) │
├──────────────────────────────────────────────────────────────┼───────────────┤
│ true                                                         │ true          │
└──────────────────────────────────────────────────────────────────────────────┘
```
