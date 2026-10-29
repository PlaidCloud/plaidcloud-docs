---
title: JSON_PATH_EXISTS (Lakehouse v1)
description: JSON_PATH_EXISTS — sprawdza, czy wskazana ścieżka istnieje w danych JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-path-exists.md
---

Sprawdza, czy wskazana ścieżka istnieje w danych JSON.

## Składnia Analyze

```python
func.json_path_exists(<json_data>, <json_path_expression)
```

## Przykłady Analyze

```python
func.json_path_exists(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ == 1)'), func.json_path_exists(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ > 1)')
┌─────────────────────────────┐
│       Item 1   │  Item 2    │
├────────────────┼────────────┤
│       True     │  False     │
└─────────────────────────────┘
```

## Składnia SQL

```sql
JSON_PATH_EXISTS(<json_data>, <json_path_expression>)
```

- json_data: określa dane JSON, w których chcesz szukać. Może to być obiekt JSON lub tablica.

- json_path_expression: określa ścieżkę, zaczynając od korzenia danych JSON reprezentowanego przez `$`, którą chcesz sprawdzić w danych JSON. W wyrażeniu możesz też umieścić warunki, używając `@` do wskazania bieżącego węzła lub elementu, który jest oceniany, aby filtrować wyniki.

## Typ zwracany

Funkcja zwraca:

- `true`, jeśli wskazana ścieżka JSON (oraz warunki, jeśli są) istnieje w danych JSON.
- `false`, jeśli wskazana ścieżka JSON (oraz warunki, jeśli są) nie istnieje w danych JSON.
- NULL, jeśli json_data lub json_path_expression ma wartość NULL lub jest nieprawidłowe.

## Przykłady SQL

```sql
SELECT JSON_PATH_EXISTS(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ == 1)');

----
true


SELECT JSON_PATH_EXISTS(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ > 1)');

----
false

SELECT JSON_PATH_EXISTS(NULL, '$.a');

----
NULL

SELECT JSON_PATH_EXISTS(parse_json('{"a": 1, "b": 2}'), NULL);

----
NULL
```
