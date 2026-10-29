---
title: GET_PATH (Lakehouse v1)
description: GET_PATH — Extrait la valeur d'un VARIANT à partir de path_name.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/get-path.md
---

Extrait la valeur d'un `VARIANT` à partir de `path_name`.
La valeur est renvoyée sous forme de `Variant`, ou `NULL` si l'un des arguments est `NULL`.

`GET_PATH` équivaut à une chaîne de fonctions `GET` ; `path_name` est constitué d'une concaténation de noms de champ précédés de points (.), de deux-points (:) ou d'opérateurs d'index (`[index]`). Le premier nom de champ ne nécessite pas d'identifiant initial.

## Syntaxe Analyze

```python
func.get_path(<variant>, <path_name>)
```

## Exemples Analyze

```python
func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k4')
┌─────────────────────────────────────────────────────────────────────────────────┐
│ func.get_path(func.parse_json('{"k1":[0,1,2], "k2":{"k3":3,"k4":4}}'), 'k2.k4') │
├─────────────────────────────────────────────────────────────────────────────────┤
│ 4                                                                               │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
GET_PATH( <variant>, <path_name> )
```

## Arguments

| Arguments     | Description                                                          |
|---------------|----------------------------------------------------------------------|
| `<variant>`   | La valeur VARIANT contenant un ARRAY ou un OBJECT                    |
| `<path_name>` | La valeur de type chaîne constituée d'une concaténation de noms de champ |

## Type de retour

VARIANT

## Exemples SQL

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
