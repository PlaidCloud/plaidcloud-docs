---
title: JSON_OBJECT_KEYS (Lakehouse v1)
description: JSON_OBJECT_KEYS — devuelve un arreglo con la lista de claves de la entrada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-keys.md
---

Devuelve un arreglo con la lista de claves del OBJECT Variant de entrada.


## Sintaxis de Analyze

```python
func.json_object_keys(<variant>)
```

## Ejemplos de Analyze

```python
func.json_object_keys(func.parse_json(parse_json('{"a": 1, "b": [1,2,3]}')), func.json_object_keys(func.parse_json(parse_json('{"b": [2,3,4]}'))
┌─────────────────────────────────────────────────────────────────┐
│       id       │  json_object_keys(var) │ json_object_keys(var) │
├────────────────┼────────────────────────┼───────────────────────┤
│              1 │ ["a","b"]              │ ["a","b"]             │
│              2 │ ["b"]                  │ ["b"]                 │
└─────────────────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
JSON_OBJECT_KEYS(<variant>)
```

## Argumentos

| Argumentos  | Descripción                                |
|-------------|--------------------------------------------|
| `<variant>` | El valor VARIANT que contiene un OBJECT    |

## Alias

- [OBJECT_KEYS](../object-keys)

## Tipo de retorno

Array`<String>`

## Ejemplos de SQL

```sql
CREATE TABLE IF NOT EXISTS objects_test1(id TINYINT, var VARIANT);

INSERT INTO
  objects_test1
VALUES
  (1, parse_json('{"a": 1, "b": [1,2,3]}'));

INSERT INTO
  objects_test1
VALUES
  (2, parse_json('{"b": [2,3,4]}'));

SELECT
  id,
  object_keys(var),
  json_object_keys(var)
FROM
  objects_test1;

┌────────────────────────────────────────────────────────────┐
│       id       │  object_keys(var) │ json_object_keys(var) │
├────────────────┼───────────────────┼───────────────────────┤
│              1 │ ["a","b"]         │ ["a","b"]             │
│              2 │ ["b"]             │ ["b"]                 │
└────────────────────────────────────────────────────────────┘
```
