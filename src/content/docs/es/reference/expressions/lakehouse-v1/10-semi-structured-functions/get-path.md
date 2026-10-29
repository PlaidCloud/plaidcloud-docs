---
title: GET_PATH (Lakehouse v1)
description: GET_PATH — Extrae un valor de un VARIANT a partir de path_name.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/get-path.md
---

Extrae un valor de un `VARIANT` a partir de `path_name`.
El valor se devuelve como `Variant`, o como `NULL` si alguno de los argumentos es `NULL`.

`GET_PATH` equivale a una cadena de funciones `GET`; `path_name` se compone de una concatenación de nombres de campo precedidos por puntos (.), dos puntos (:) u operadores de índice (`[index]`). El primer nombre de campo no requiere que se especifique el identificador inicial.

## Sintaxis de Analyze

```python
func.get_path(<variant>, <path_name>)
```

## Ejemplos de Analyze

```python
func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k4')
┌─────────────────────────────────────────────────────────────────────────────────┐
│ func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k4') │
├─────────────────────────────────────────────────────────────────────────────────┤
│ 4                                                                               │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
GET_PATH( <variant>, <path_name> )
```

## Argumentos

| Argumentos    | Descripción                                                                   |
|---------------|-------------------------------------------------------------------------------|
| `<variant>`   | El valor VARIANT que contiene un ARRAY o un OBJECT                            |
| `<path_name>` | El valor de tipo cadena que consiste en una concatenación de nombres de campo |

## Tipo de retorno

VARIANT

## Ejemplos de SQL

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
