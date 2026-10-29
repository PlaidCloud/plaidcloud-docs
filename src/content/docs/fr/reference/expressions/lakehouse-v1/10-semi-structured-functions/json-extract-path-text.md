---
title: JSON_EXTRACT_PATH_TEXT (Lakehouse v1)
description: JSON_EXTRACT_PATH_TEXT — extrait la valeur d'une chaîne JSON à partir de path_name.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-extract-path-text.md
---

Extrait la valeur d'une chaîne JSON à partir de `path_name`.
La valeur est renvoyée sous forme de `String`, ou `NULL` si l'un des arguments est `NULL`.
Cette fonction équivaut à `to_varchar(GET_PATH(PARSE_JSON(JSON), PATH_NAME))`.

## Syntaxe Analyze

```python
func.json_extract_path_text(<expr>, <path_name>)
```

## Exemples Analyze

```python
func.json_extract_path_text('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}', 'k2.k4')
┌──────────────────────────────────────────────────────────────────────────────┐
│ func.json_extract_path_text('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}', 'k2.k4') │
├──────────────────────────────────────────────────────────────────────────────┤
│ 4                                                                            │
└──────────────────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
JSON_EXTRACT_PATH_TEXT( <expr>, <path_name> )
```

## Arguments

| Arguments     | Description                                                              |
|---------------|--------------------------------------------------------------------------|
| `<expr>`      | La valeur de type chaîne JSON                                            |
| `<path_name>` | La valeur de type chaîne constituée d'une concaténation de noms de champ |

## Type de retour

Chaîne

## Exemples SQL

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
