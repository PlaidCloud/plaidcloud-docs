---
title: JSON_EXTRACT_PATH_TEXT (Lakehouse v1)
description: JSON_EXTRACT_PATH_TEXT — Extrahiert anhand von path_name einen Wert aus einer JSON-Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-extract-path-text.md
---

Extrahiert anhand von `path_name` einen Wert aus einer JSON-Zeichenfolge.
Der Wert wird als `String` zurückgegeben, oder als `NULL`, wenn eines der Argumente `NULL` ist.
Diese Funktion entspricht `to_varchar(GET_PATH(PARSE_JSON(JSON), PATH_NAME))`.

## Analyze Syntax

```python
func.json_extract_path_text(<expr>, <path_name>)
```

## Analyze Examples

```python
func.json_extract_path_text('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}', 'k2.k4')
┌──────────────────────────────────────────────────────────────────────────────┐
│ func.json_extract_path_text('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}', 'k2.k4') │
├──────────────────────────────────────────────────────────────────────────────┤
│ 4                                                                            │
└──────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
JSON_EXTRACT_PATH_TEXT( <expr>, <path_name> )
```

## Arguments

| Argumente     | Beschreibung                                                          |
|---------------|-----------------------------------------------------------------------|
| `<expr>`      | Der JSON-Zeichenfolgenwert                                            |
| `<path_name>` | Der Zeichenfolgenwert, der aus aneinandergereihten Feldnamen besteht  |

## Return Type

String

## SQL Examples

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
