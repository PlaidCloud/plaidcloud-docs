---
title: JSON_EACH (Lakehouse v1)
description: JSON_EACH — wyodrębnia pary klucz-wartość z obiektu JSON, rozbijając strukturę na poszczególne wiersze zbioru wyników.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-each.md
---

Wyodrębnia pary klucz-wartość z obiektu JSON, rozbijając strukturę na poszczególne wiersze zbioru wyników. Każdy wiersz reprezentuje jedną parę klucz-wartość pochodzącą z wejściowego wyrażenia JSON.

## Składnia Analyze

```python
func.json_each(<json_string>)
```

## Przykłady Analyze

```python

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.json_each(func.parse_json('{"name": "john", "age": 25, "isstudent": false, "grades": [90, 85, 92]}')) │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ ('age','25')                                                                                               │
│ ('grades','[90,85,92]')                                                                                    │
│ ('isStudent','false')                                                                                      │
│ ('name','"John"')                                                                                          │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
JSON_EACH(<json_string>)
```

## Typ zwracany

JSON_EACH zwraca zbiór krotek, z których każda składa się z klucza typu STRING i odpowiadającej mu wartości typu VARIANT.

## Przykłady SQL

```sql
-- Extract key-value pairs from a JSON object representing information about a person
SELECT
  JSON_EACH(
    PARSE_JSON (
      '{"name": "John", "age": 25, "isStudent": false, "grades": [90, 85, 92]}'
    )
  );


┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ json_each(parse_json('{"name": "john", "age": 25, "isstudent": false, "grades": [90, 85, 92]}')) │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ ('age','25')                                                                                     │
│ ('grades','[90,85,92]')                                                                          │
│ ('isStudent','false')                                                                            │
│ ('name','"John"')                                                                                │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘

-- Display data types of the extracted values
SELECT
  TYPEOF (
    JSON_EACH(
      PARSE_JSON (
        '{"name": "John", "age": 25, "isStudent": false, "grades": [90, 85, 92]}'
      )
    )
  );

┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ typeof(json_each(parse_json('{"name": "john", "age": 25, "isstudent": false, "grades": [90, 85, 92]}'))) │
├──────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ TUPLE(STRING, VARIANT) NULL                                                                              │
│ TUPLE(STRING, VARIANT) NULL                                                                              │
│ TUPLE(STRING, VARIANT) NULL                                                                              │
│ TUPLE(STRING, VARIANT) NULL                                                                              │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
