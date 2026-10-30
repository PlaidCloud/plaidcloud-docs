---
title: GET_PATH (Lakehouse v1)
description: GET_PATH — Extrahiert anhand von path_name einen Wert aus einer VARIANT.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/get-path.md
---

Extrahiert anhand von `path_name` einen Wert aus einer `VARIANT`.
Der Wert wird als `Variant` zurückgegeben, oder als `NULL`, wenn eines der Argumente `NULL` ist.

`GET_PATH` entspricht einer Kette von `GET`-Funktionen. `path_name` besteht aus aneinandergereihten Feldnamen, denen jeweils ein Punkt (.), ein Doppelpunkt (:) oder ein Indexoperator (`[index]`) vorangestellt ist. Beim ersten Feldnamen muss das führende Zeichen nicht angegeben werden.

## Analyze Syntax

```python
func.get_path(<variant>, <path_name>)
```

## Analyze Examples

```python
func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k4')
┌─────────────────────────────────────────────────────────────────────────────────┐
│ func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k4') │
├─────────────────────────────────────────────────────────────────────────────────┤
│ 4                                                                               │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
GET_PATH( <variant>, <path_name> )
```

## Arguments

| Argumente     | Beschreibung                                                          |
|---------------|-----------------------------------------------------------------------|
| `<variant>`   | Der VARIANT-Wert, der entweder ein ARRAY oder ein OBJECT enthält      |
| `<path_name>` | Der Zeichenfolgenwert, der aus aneinandergereihten Feldnamen besteht  |

## Return Type

VARIANT

## SQL Examples

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
