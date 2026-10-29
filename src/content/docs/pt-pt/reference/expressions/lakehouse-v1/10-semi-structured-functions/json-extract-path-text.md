---
title: JSON_EXTRACT_PATH_TEXT (Lakehouse v1)
description: JSON_EXTRACT_PATH_TEXT — extrai o valor de uma cadeia JSON através de path_name.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-extract-path-text.md
---

Extrai o valor de uma cadeia JSON através de `path_name`.
O valor é devolvido como `String` ou `NULL` se qualquer um dos argumentos for `NULL`.
Esta função equivale a `to_varchar(GET_PATH(PARSE_JSON(JSON), PATH_NAME))`.

## Sintaxe do Analyze

```python
func.json_extract_path_text(<expr>, <path_name>)
```

## Exemplos do Analyze

```python
func.json_extract_path_text('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}', 'k2.k4')
┌──────────────────────────────────────────────────────────────────────────────┐
│ func.json_extract_path_text('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}', 'k2.k4') │
├──────────────────────────────────────────────────────────────────────────────┤
│ 4                                                                            │
└──────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
JSON_EXTRACT_PATH_TEXT( <expr>, <path_name> )
```

## Argumentos

| Argumentos    | Descrição                                                           |
|---------------|---------------------------------------------------------------------|
| `<expr>`      | O valor de cadeia JSON                                              |
| `<path_name>` | O valor de cadeia que consiste numa concatenação de nomes de campos |

## Tipo de retorno

Cadeia

## Exemplos de SQL

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
