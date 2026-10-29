---
title: "GET (Semi-Structured, Lakehouse v1)"
description: GET — wyodrębnia wartość z Variant zawierającego ARRAY według indeksu lub z Variant zawierającego OBJECT według nazwy pola.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/get.md
---

Wyodrębnia wartość z `Variant` zawierającego `ARRAY` według `index` lub z `Variant` zawierającego `OBJECT` według `field_name`.
Wartość jest zwracana jako `Variant` lub `NULL`, jeśli którykolwiek z argumentów ma wartość `NULL`.

`GET` stosuje do `field_name` dopasowanie z rozróżnianiem wielkości liter. Aby dopasować bez rozróżniania wielkości liter, użyj `GET_IGNORE_CASE`.

## Składnia Analyze

```python
func.get(<variant>, <index>)

or

func.get(<variant>, <field_name>)
```

## Przykłady Analyze

```python
func.get(func.parse_json('[2.71, 3.14]'), 0);
┌──────────────────────────────────────────────┐
│ func.get(func.parse_json('[2.71, 3.14]'), 0) │
├──────────────────────────────────────────────┤
│ 2.71                                         │
└──────────────────────────────────────────────┘


func.get(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'aa');
┌─────────────────────────────────────────────────────────────┐
│ func.get(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'aa') │
├─────────────────────────────────────────────────────────────┤
│ 1                                                           │
└─────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
GET( <variant>, <index> )

GET( <variant>, <field_name> )
```

## Argumenty

| Argumenty      | Opis                                                                   |
|----------------|------------------------------------------------------------------------|
| `<variant>`    | Wartość VARIANT zawierająca ARRAY lub OBJECT                           |
| `<index>`      | Wartość Uint32 określająca położenie wartości w ARRAY                  |
| `<field_name>` | Wartość typu String określająca klucz w parze klucz-wartość obiektu OBJECT |

## Typ zwracany

VARIANT

## Przykłady SQL

```sql
SELECT get(parse_json('[2.71, 3.14]'), 0);
┌────────────────────────────────────┐
│ get(parse_json('[2.71, 3.14]'), 0) │
├────────────────────────────────────┤
│ 2.71                               │
└────────────────────────────────────┘

SELECT get(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'aa');
┌───────────────────────────────────────────────────┐
│ get(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'aa') │
├───────────────────────────────────────────────────┤
│ 1                                                 │
└───────────────────────────────────────────────────┘

SELECT get(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA');
┌───────────────────────────────────────────────────┐
│ get(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA') │
├───────────────────────────────────────────────────┤
│ NULL                                              │
└───────────────────────────────────────────────────┘
```
