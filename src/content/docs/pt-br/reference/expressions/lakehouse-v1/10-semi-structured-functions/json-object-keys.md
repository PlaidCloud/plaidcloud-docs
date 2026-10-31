---
title: JSON_OBJECT_KEYS (Lakehouse v1)
description: JSON_OBJECT_KEYS — retorna um Array com a lista de chaves da entrada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-keys.md
---

Retorna um Array com a lista de chaves do OBJECT Variant de entrada.


## Sintaxe do Analyze

```python
func.json_object_keys(<variant>)
```

## Exemplos do Analyze

```python
func.json_object_keys(func.parse_json(parse_json('{"a": 1, "b": [1,2,3]}')), func.json_object_keys(func.parse_json(parse_json('{"b": [2,3,4]}'))
┌─────────────────────────────────────────────────────────────────┐
│       id       │  json_object_keys(var) │ json_object_keys(var) │
├────────────────┼────────────────────────┼───────────────────────┤
│              1 │ ["a","b"]              │ ["a","b"]             │
│              2 │ ["b"]                  │ ["b"]                 │
└─────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
JSON_OBJECT_KEYS(<variant>)
```

## Argumentos

| Argumentos  | Descrição                                 |
|-------------|-------------------------------------------|
| `<variant>` | O valor VARIANT que contém um OBJECT      |

## Aliases

- [OBJECT_KEYS](../object-keys)

## Tipo de retorno

Array`<String>`

## Exemplos de SQL

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
