---
title: GET_IGNORE_CASE (Lakehouse v1)
description: GET_IGNORE_CASE — wyodrębnia z wartości VARIANT zawierającej OBJECT wartość wskazaną przez field_name.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/get-ignore-case.md
---

Wyodrębnia z wartości `VARIANT` zawierającej `OBJECT` wartość wskazaną przez field_name.
Wartość jest zwracana jako `Variant` lub `NULL`, jeśli którykolwiek z argumentów ma wartość `NULL`.

`GET_IGNORE_CASE` działa podobnie do `GET`, ale stosuje do nazw pól dopasowanie bez rozróżniania wielkości liter.
Najpierw dopasowywana jest dokładnie taka sama nazwa pola, a jeśli nie zostanie znaleziona, dopasowywana jest nazwa pola bez rozróżniania wielkości liter, w kolejności alfabetycznej.

## Składnia Analyze

```python
func.get_ignore_Case(<variant>, <field_name>)
```

## Przykłady Analyze

```python
func.get_ignore_case(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA')
┌─────────────────────────────────────────────────────────────────────────┐
│ func.get_ignore_case(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA') │
├─────────────────────────────────────────────────────────────────────────┤
│ 3                                                                       │
└─────────────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
GET_IGNORE_CASE( <variant>, <field_name> )
```

## Argumenty

| Argumenty      | Opis                                                                |
|----------------|---------------------------------------------------------------------|
| `<variant>`    | Wartość VARIANT zawierająca ARRAY lub OBJECT                        |
| `<field_name>` | Wartość typu String określająca klucz w parze klucz-wartość obiektu OBJECT |

## Typ zwracany

VARIANT

## Przykłady SQL

```sql
SELECT get_ignore_case(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA');
┌───────────────────────────────────────────────────────────────┐
│ get_ignore_case(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA') │
├───────────────────────────────────────────────────────────────┤
│ 3                                                             │
└───────────────────────────────────────────────────────────────┘
```
