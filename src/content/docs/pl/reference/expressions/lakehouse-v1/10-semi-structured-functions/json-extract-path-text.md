---
title: JSON_EXTRACT_PATH_TEXT (Lakehouse v1)
description: JSON_EXTRACT_PATH_TEXT — wyodrębnia z ciągu JSON wartość wskazaną przez path_name.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-extract-path-text.md
---

Wyodrębnia z ciągu JSON wartość wskazaną przez `path_name`.
Wartość jest zwracana jako `String` lub `NULL`, jeśli którykolwiek z argumentów ma wartość `NULL`.
Ta funkcja jest równoważna `to_varchar(GET_PATH(PARSE_JSON(JSON), PATH_NAME))`.

## Składnia Analyze

```python
func.json_extract_path_text(<expr>, <path_name>)
```

## Przykłady Analyze

```python
func.json_extract_path_text('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}', 'k2.k4')
┌──────────────────────────────────────────────────────────────────────────────┐
│ func.json_extract_path_text('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}', 'k2.k4') │
├──────────────────────────────────────────────────────────────────────────────┤
│ 4                                                                            │
└──────────────────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
JSON_EXTRACT_PATH_TEXT( <expr>, <path_name> )
```

## Argumenty

| Argumenty     | Opis                                                             |
|---------------|------------------------------------------------------------------|
| `<expr>`      | Wartość typu ciąg JSON                                           |
| `<path_name>` | Wartość typu String składająca się z połączonych nazw pól        |

## Typ zwracany

String

## Przykłady SQL

```sql
SELECT json_extract_path_text('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}', 'k1[0]');
┌─────────────────────────────────────────────────────────────────────────┐
│ json_extract_path_text('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}', 'k1[0]') │
├─────────────────────────────────────────────────────────────────────────┤
│ 0                                                                       │
└─────────────────────────────────────────────────────────────────────────┘

SELECT json_extract_path_text('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}', 'k2:k3');
┌─────────────────────────────────────────────────────────────────────────┐
│ json_extract_path_text('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}', 'k2:k3') │
├─────────────────────────────────────────────────────────────────────────┤
│ 3                                                                       │
└─────────────────────────────────────────────────────────────────────────┘

SELECT json_extract_path_text('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}', 'k2.k4');
┌─────────────────────────────────────────────────────────────────────────┐
│ json_extract_path_text('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}', 'k2.k4') │
├─────────────────────────────────────────────────────────────────────────┤
│ 4                                                                       │
└─────────────────────────────────────────────────────────────────────────┘

SELECT json_extract_path_text('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}', 'k2.k5');
┌─────────────────────────────────────────────────────────────────────────┐
│ json_extract_path_text('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}', 'k2.k5') │
├─────────────────────────────────────────────────────────────────────────┤
│ NULL                                                                    │
└─────────────────────────────────────────────────────────────────────────┘
```
