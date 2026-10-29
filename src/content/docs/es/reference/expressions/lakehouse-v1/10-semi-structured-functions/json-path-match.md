---
title: JSON_PATH_MATCH (Lakehouse v1)
description: JSON_PATH_MATCH — comprueba si una expresión de ruta JSON especificada cumple ciertas condiciones.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-path-match.md
---

Comprueba si una expresión de ruta JSON especificada cumple ciertas condiciones dentro de unos datos JSON. Tenga en cuenta que el operador `@@` es sinónimo de esta función. Para obtener más información, consulte Operadores JSON.


## Sintaxis de Analyze

```python
func.json_path_match(<json_data>, <json_path_expression)
```

## Ejemplos de Analyze

```python
func.json_path_match(func.parse_json('{"a":1,"b":[1,2,3]}'), '$.a == 1')
┌──────────────────────────────────────────────────────────────────────────┐
│ func.json_path_match(func.parse_json('{"a":1,"b":[1,2,3]}'), '$.a == 1') │
├──────────────────────────────────────────────────────────────────────────┤
│ true                                                                     │
└──────────────────────────────────────────────────────────────────────────┘

func.json_path_match(func.parse_json('{"a":1,"b":[1,2,3]}'), '$.b[0] > 1')
┌────────────────────────────────────────────────────────────────────────────┐
│ func.json_path_match(func.parse_json('{"a":1,"b":[1,2,3]}'), '$.b[0] > 1') │
├────────────────────────────────────────────────────────────────────────────┤
│ false                                                                      │
└────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
JSON_PATH_MATCH(<json_data>, <json_path_expression>)
```

- `json_data`: especifica los datos JSON que desea examinar. Puede ser un objeto JSON o un arreglo.
- `json_path_expression`: especifica las condiciones que se comprobarán dentro de los datos JSON. Esta expresión describe la ruta o los criterios concretos que deben cumplirse, por ejemplo, verificar si determinados valores de campo de la estructura JSON cumplen ciertas condiciones. El símbolo `$` representa la raíz de los datos JSON. Se utiliza para iniciar la expresión de ruta e indica el objeto de nivel superior de la estructura JSON.

## Tipo de retorno

La función devuelve:

- `true` si la expresión de ruta JSON especificada cumple las condiciones dentro de los datos JSON.
- `false` si la expresión de ruta JSON especificada no cumple las condiciones dentro de los datos JSON.
- NULL si `json_data` o `json_path_expression` es NULL o no es válido.

## Ejemplos de SQL

```sql
-- Check if the value at JSON path $.a is equal to 1
SELECT JSON_PATH_MATCH(parse_json('{"a":1,"b":[1,2,3]}'), '$.a == 1');

┌────────────────────────────────────────────────────────────────┐
│ json_path_match(parse_json('{"a":1,"b":[1,2,3]}'), '$.a == 1') │
├────────────────────────────────────────────────────────────────┤
│ true                                                           │
└────────────────────────────────────────────────────────────────┘

-- Check if the first element in the array at JSON path $.b is greater than 1
SELECT JSON_PATH_MATCH(parse_json('{"a":1,"b":[1,2,3]}'), '$.b[0] > 1');

┌──────────────────────────────────────────────────────────────────┐
│ json_path_match(parse_json('{"a":1,"b":[1,2,3]}'), '$.b[0] > 1') │
├──────────────────────────────────────────────────────────────────┤
│ false                                                            │
└──────────────────────────────────────────────────────────────────┘

-- Check if any element in the array at JSON path $.b
-- from the second one to the last are greater than or equal to 2
SELECT JSON_PATH_MATCH(parse_json('{"a":1,"b":[1,2,3]}'), '$.b[1 to last] >= 2');

┌───────────────────────────────────────────────────────────────────────────┐
│ json_path_match(parse_json('{"a":1,"b":[1,2,3]}'), '$.b[1 to last] >= 2') │
├───────────────────────────────────────────────────────────────────────────┤
│ true                                                                      │
└───────────────────────────────────────────────────────────────────────────┘

-- NULL is returned if either the json_data or json_path_expression is NULL or invalid.
SELECT JSON_PATH_MATCH(parse_json('{"a":1,"b":[1,2,3]}'), NULL);

┌──────────────────────────────────────────────────────────┐
│ json_path_match(parse_json('{"a":1,"b":[1,2,3]}'), null) │
├──────────────────────────────────────────────────────────┤
│ NULL                                                     │
└──────────────────────────────────────────────────────────┘

SELECT JSON_PATH_MATCH(NULL, '$.a == 1');

┌───────────────────────────────────┐
│ json_path_match(null, '$.a == 1') │
├───────────────────────────────────┤
│ NULL                              │
└───────────────────────────────────┘
```
