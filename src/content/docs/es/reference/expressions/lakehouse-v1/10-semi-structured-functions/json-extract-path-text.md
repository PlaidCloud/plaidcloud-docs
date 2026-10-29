---
title: JSON_EXTRACT_PATH_TEXT (Lakehouse v1)
description: JSON_EXTRACT_PATH_TEXT — extrae un valor de una cadena JSON a partir de path_name.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-extract-path-text.md
---

Extrae un valor de una cadena JSON a partir de `path_name`.
El valor se devuelve como `String`, o como `NULL` si alguno de los argumentos es `NULL`.
Esta función equivale a `to_varchar(GET_PATH(PARSE_JSON(JSON), PATH_NAME))`.

## Sintaxis de Analyze

```python
func.json_extract_path_text(<expr>, <path_name>)
```

## Ejemplos de Analyze

```python
func.json_extract_path_text('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}', 'k2.k4')
┌──────────────────────────────────────────────────────────────────────────────┐
│ func.json_extract_path_text('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}', 'k2.k4') │
├──────────────────────────────────────────────────────────────────────────────┤
│ 4                                                                            │
└──────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
JSON_EXTRACT_PATH_TEXT( <expr>, <path_name> )
```

## Argumentos

| Argumentos    | Descripción                                                                   |
|---------------|-------------------------------------------------------------------------------|
| `<expr>`      | El valor de cadena JSON                                                       |
| `<path_name>` | El valor de tipo cadena que consiste en una concatenación de nombres de campo |

## Tipo de retorno

String

## Ejemplos de SQL

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
