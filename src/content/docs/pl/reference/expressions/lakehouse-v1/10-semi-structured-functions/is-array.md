---
title: IS_ARRAY (Lakehouse v1)
description: IS_ARRAY — sprawdza, czy wartość wejściowa jest tablicą JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-array.md
---

Sprawdza, czy wartość wejściowa jest tablicą JSON. Uwaga: tablica JSON to nie to samo co typ danych ARRAY. Tablica JSON to struktura danych powszechnie używana w formacie JSON, reprezentująca uporządkowaną kolekcję wartości ujętych w nawiasy kwadratowe `[ ]`. Jest to elastyczny format organizowania i wymiany różnych typów danych, w tym ciągów znaków, liczb, wartości logicznych, obiektów i wartości null. 

```json title='JSON Array Example:'
[
  "Apple",
  42,
  true,
  {"name": "John", "age": 30, "isStudent": false},
  [1, 2, 3],
  null
]
```

## Składnia Analyze

```python
func.is_array(<expr>)
```

## Przykłady Analyze

```python

func.is_array(func.parse_json('true')), func.is_array(func.parse_json('[1,2,3]'))
┌────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_array(func.parse_json('true')) │ func.is_array(func.parse_json('[1,2,3]')) │
├────────────────────────────────────────┼───────────────────────────────────────────┤
│ false                                  │ true                                      │
└────────────────────────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
IS_ARRAY( <expr> )
```

## Typ zwracany

Zwraca `true`, jeśli wartość wejściowa jest tablicą JSON, a w przeciwnym razie `false`.

## Przykłady SQL

```sql
SELECT
  IS_ARRAY(PARSE_JSON('true')),
  IS_ARRAY(PARSE_JSON('[1,2,3]'));

┌────────────────────────────────────────────────────────────────┐
│ is_array(parse_json('true')) │ is_array(parse_json('[1,2,3]')) │
├──────────────────────────────┼─────────────────────────────────┤
│ false                        │ true                            │
└────────────────────────────────────────────────────────────────┘
```
