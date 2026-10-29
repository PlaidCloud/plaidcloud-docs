---
title: JSON_PATH_EXISTS (Lakehouse v1)
description: JSON_PATH_EXISTS — comprueba si existe una ruta especificada en datos JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-path-exists.md
---

Comprueba si existe una ruta especificada en datos JSON.

## Sintaxis de Analyze

```python
func.json_path_exists(<json_data>, <json_path_expression)
```

## Ejemplos de Analyze

```python
func.json_path_exists(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ == 1)'), func.json_path_exists(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ > 1)')
┌─────────────────────────────┐
│       Item 1   │  Item 2    │
├────────────────┼────────────┤
│       True     │  False     │
└─────────────────────────────┘
```

## Sintaxis SQL

```sql
JSON_PATH_EXISTS(<json_data>, <json_path_expression>)
```

- json_data: especifica los datos JSON en los que desea buscar. Puede ser un objeto JSON o un arreglo.

- json_path_expression: especifica la ruta, a partir de la raíz de los datos JSON representada por `$`, que desea comprobar dentro de los datos JSON. También puede incluir condiciones en la expresión, usando `@` para referirse al nodo o elemento actual que se evalúa, para filtrar los resultados.

## Tipo de retorno

La función devuelve:

- `true` si la ruta JSON especificada (y las condiciones, si las hay) existe dentro de los datos JSON.
- `false` si la ruta JSON especificada (y las condiciones, si las hay) no existe dentro de los datos JSON.
- NULL si json_data o json_path_expression es NULL o no es válido.

## Ejemplos de SQL

```sql
SELECT JSON_PATH_EXISTS(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ == 1)');

----
true


SELECT JSON_PATH_EXISTS(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ > 1)');

----
false

SELECT JSON_PATH_EXISTS(NULL, '$.a');

----
NULL

SELECT JSON_PATH_EXISTS(parse_json('{"a": 1, "b": 2}'), NULL);

----
NULL
```
