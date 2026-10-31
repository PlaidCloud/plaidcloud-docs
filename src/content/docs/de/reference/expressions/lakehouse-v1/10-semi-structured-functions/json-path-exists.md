---
title: JSON_PATH_EXISTS (Lakehouse v1)
description: JSON_PATH_EXISTS — Prüft, ob ein angegebener Pfad in JSON-Daten existiert.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-path-exists.md
---

Prüft, ob ein angegebener Pfad in JSON-Daten existiert.

## Analyze Syntax

```python
func.json_path_exists(<json_data>, <json_path_expression)
```

## Analyze Examples

```python
func.json_path_exists(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ == 1)'), func.json_path_exists(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ > 1)')
┌─────────────────────────────┐
│       Item 1   │  Item 2    │
├────────────────┼────────────┤
│       True     │  False     │
└─────────────────────────────┘
```

## SQL Syntax

```sql
JSON_PATH_EXISTS(<json_data>, <json_path_expression>)
```

- json_data: Gibt die JSON-Daten an, in denen Sie suchen möchten. Es kann ein JSON-Objekt oder ein Array sein.

- json_path_expression: Gibt den Pfad an, den Sie in den JSON-Daten prüfen möchten. Er beginnt an der Wurzel der JSON-Daten, die durch `$` dargestellt wird. Im Ausdruck können Sie auch Bedingungen angeben, um die Ergebnisse zu filtern; dabei verweist `@` auf den aktuell ausgewerteten Knoten oder das aktuell ausgewertete Element.

## Return Type

Die Funktion gibt Folgendes zurück:

- `true`, wenn der angegebene JSON-Pfad (und gegebenenfalls die Bedingungen) in den JSON-Daten existiert.
- `false`, wenn der angegebene JSON-Pfad (und gegebenenfalls die Bedingungen) in den JSON-Daten nicht existiert.
- NULL, wenn json_data oder json_path_expression NULL oder ungültig ist.

## SQL Examples

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
