---
title: IS_ARRAY (Lakehouse v1)
description: IS_ARRAY — Comprueba si el valor de entrada es un arreglo JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/is-array.md
---

Comprueba si el valor de entrada es un arreglo JSON. Tenga en cuenta que un arreglo JSON no es lo mismo que el tipo de datos ARRAY. Un arreglo JSON es una estructura de datos de uso habitual en JSON que representa una colección ordenada de valores entre corchetes `[ ]`. Es un formato flexible para organizar e intercambiar distintos tipos de datos, como cadenas, números, valores booleanos, objetos y valores nulos. 

```json title='JSON Array Example:'
[
  "Apple",
  42,
  true,
  {"name": "John", "age": 30, "isStudent": false},
  [1, 2, 3],
  null
]
```

## Sintaxis de Analyze

```python
func.is_array(<expr>)
```

## Ejemplos de Analyze

```python

func.is_array(func.parse_json('true')), func.is_array(func.parse_json('[1,2,3]'))
┌────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_array(func.parse_json('true')) │ func.is_array(func.parse_json('[1,2,3]')) │
├────────────────────────────────────────┼───────────────────────────────────────────┤
│ false                                  │ true                                      │
└────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
IS_ARRAY( <expr> )
```

## Tipo de retorno

Devuelve `true` si el valor de entrada es un arreglo JSON y `false` en caso contrario.

## Ejemplos de SQL

```sql
SELECT
  IS_ARRAY(PARSE_JSON('true')),
  IS_ARRAY(PARSE_JSON('[1,2,3]'));

┌────────────────────────────────────────────────────────────────┐
│ is_array(parse_json('true')) │ is_array(parse_json('[1,2,3]')) │
├──────────────────────────────┼─────────────────────────────────┤
│ false                        │ true                            │
└────────────────────────────────────────────────────────────────┘
```
