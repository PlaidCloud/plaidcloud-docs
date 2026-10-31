---
title: GET_PATH (Lakehouse v1)
description: GET_PATH — wyodrębnia z wartości VARIANT wartość wskazaną przez path_name.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/get-path.md
---

Wyodrębnia z wartości `VARIANT` wartość wskazaną przez `path_name`.
Wartość jest zwracana jako `Variant` lub `NULL`, jeśli którykolwiek z argumentów ma wartość `NULL`.

`GET_PATH` jest odpowiednikiem łańcucha funkcji `GET`; `path_name` składa się z połączonych nazw pól poprzedzonych kropkami (.), dwukropkami (:) lub operatorami indeksu (`[index]`). Przed pierwszą nazwą pola nie trzeba podawać znaku wiodącego.

## Składnia Analyze

```python
func.get_path(<variant>, <path_name>)
```

## Przykłady Analyze

```python
func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k4')
┌─────────────────────────────────────────────────────────────────────────────────┐
│ func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k4') │
├─────────────────────────────────────────────────────────────────────────────────┤
│ 4                                                                               │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
GET_PATH( <variant>, <path_name> )
```

## Argumenty

| Argumenty     | Opis                                                             |
|---------------|------------------------------------------------------------------|
| `<variant>`   | Wartość VARIANT zawierająca ARRAY lub OBJECT                     |
| `<path_name>` | Wartość typu String składająca się z połączonych nazw pól        |

## Typ zwracany

VARIANT

## Przykłady SQL

```sql
SELECT get_path(parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k1[0]');
┌───────────────────────────────────────────────────────────────────────┐
│ get_path(parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k1[0]') │
├───────────────────────────────────────────────────────────────────────┤
│ 0                                                                     │
└───────────────────────────────────────────────────────────────────────┘

SELECT get_path(parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2:k3');
┌───────────────────────────────────────────────────────────────────────┐
│ get_path(parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2:k3') │
├───────────────────────────────────────────────────────────────────────┤
│ 3                                                                     │
└───────────────────────────────────────────────────────────────────────┘

SELECT get_path(parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k4');
┌───────────────────────────────────────────────────────────────────────┐
│ get_path(parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k4') │
├───────────────────────────────────────────────────────────────────────┤
│ 4                                                                     │
└───────────────────────────────────────────────────────────────────────┘

SELECT get_path(parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k5');
┌───────────────────────────────────────────────────────────────────────┐
│ get_path(parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k5') │
├───────────────────────────────────────────────────────────────────────┤
│ NULL                                                                  │
└───────────────────────────────────────────────────────────────────────┘
```
