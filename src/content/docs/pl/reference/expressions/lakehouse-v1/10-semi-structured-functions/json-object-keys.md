---
title: JSON_OBJECT_KEYS (Lakehouse v1)
description: JSON_OBJECT_KEYS — zwraca tablicę zawierającą listę kluczy z danych wejściowych.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-keys.md
---

Zwraca tablicę zawierającą listę kluczy z wejściowego obiektu OBJECT typu Variant.


## Składnia Analyze

```python
func.json_object_keys(<variant>)
```

## Przykłady Analyze

```python
func.json_object_keys(func.parse_json(parse_json('{"a": 1, "b": [1,2,3]}')), func.json_object_keys(func.parse_json(parse_json('{"b": [2,3,4]}'))
┌─────────────────────────────────────────────────────────────────┐
│       id       │  json_object_keys(var) │ json_object_keys(var) │
├────────────────┼────────────────────────┼───────────────────────┤
│              1 │ ["a","b"]              │ ["a","b"]             │
│              2 │ ["b"]                  │ ["b"]                 │
└─────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
JSON_OBJECT_KEYS(<variant>)
```

## Argumenty

| Argumenty   | Opis                                       |
|-------------|--------------------------------------------|
| `<variant>` | Wartość VARIANT zawierająca OBJECT         |

## Aliasy

- [OBJECT_KEYS](../object-keys)

## Typ zwracany

Array`<String>`

## Przykłady SQL

```sql
CREATE TABLE IF NOT EXISTS objects_test1(id TINYINT, var VARIANT);

INSERT INTO
  objects_test1
VALUES
  (1, parse_json('{"a": 1, "b": [1,2,3]}'));

INSERT INTO
  objects_test1
VALUES
  (2, parse_json('{"b": [2,3,4]}'));

SELECT
  id,
  object_keys(var),
  json_object_keys(var)
FROM
  objects_test1;

┌────────────────────────────────────────────────────────────┐
│       id       │  object_keys(var) │ json_object_keys(var) │
├────────────────┼───────────────────┼───────────────────────┤
│              1 │ ["a","b"]         │ ["a","b"]             │
│              2 │ ["b"]             │ ["b"]                 │
└────────────────────────────────────────────────────────────┘
```
