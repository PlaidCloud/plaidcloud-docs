---
title: GET_PATH (Lakehouse v1)
description: GET_PATH — Extrai o valor de um VARIANT por path_name.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/get-path.md
---

Extrai o valor de um `VARIANT` por `path_name`.
O valor é retornado como `Variant`, ou `NULL` se qualquer um dos argumentos for `NULL`.

`GET_PATH` equivale a uma cadeia de funções `GET`; `path_name` consiste em uma concatenação de nomes de campo precedidos por pontos (.), dois-pontos (:) ou operadores de índice (`[index]`). O primeiro nome de campo não exige que o identificador inicial seja especificado.

## Sintaxe do Analyze

```python
func.get_path(<variant>, <path_name>)
```

## Exemplos do Analyze

```python
func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k4')
┌─────────────────────────────────────────────────────────────────────────────────┐
│ func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k4') │
├─────────────────────────────────────────────────────────────────────────────────┤
│ 4                                                                               │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
GET_PATH( <variant>, <path_name> )
```

## Argumentos

| Argumentos    | Descrição                                                        |
|---------------|------------------------------------------------------------------|
| `<variant>`   | O valor VARIANT que contém um ARRAY ou um OBJECT                 |
| `<path_name>` | O valor String que consiste em uma concatenação de nomes de campo |

## Tipo de retorno

VARIANT

## Exemplos de SQL

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
