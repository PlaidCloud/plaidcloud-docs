---
title: JQ (Lakehouse v1)
description: JQ — la función JQ es una función SQL que devuelve un conjunto de filas y permite aplicar jq.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/jq.md
---

La función JQ es una función SQL que devuelve un conjunto de filas y permite aplicar filtros de [jq](https://jqlang.github.io/jq/) a datos JSON almacenados en columnas Variant. Con esta función puede procesar datos JSON aplicando un filtro jq especificado y obtener los resultados como un conjunto de filas.

## Sintaxis SQL

```sql
JQ (<jq_expression>, <json_data>)
```

| Parámetro       | Descripción                                                                                                                                                                                                                                                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `jq_expression` | Una expresión de filtro `jq` que define cómo procesar y transformar datos JSON con la sintaxis de `jq`. Esta expresión puede especificar cómo seleccionar, modificar y manipular datos dentro de objetos y arreglos JSON. Para obtener información sobre la sintaxis, los filtros y las funciones que admite jq, consulte el [manual de jq](https://jqlang.github.io/jq/manual/#basic-filters). |
| `json_data`     | La entrada en formato JSON que desea procesar o transformar con la expresión de filtro `jq`. Puede ser un objeto JSON, un arreglo o cualquier estructura de datos JSON válida.                                                                                                                                                                              |

## Tipo de retorno

La función JQ devuelve un conjunto de valores JSON, donde cada valor corresponde a un elemento del resultado transformado o extraído según `<jq_expression>`.

## Ejemplos de SQL

Para empezar, creamos una tabla llamada `customer_data` con las columnas `id` y `profile`, donde `profile` es de tipo JSON para almacenar la información de los usuarios:

```sql
CREATE TABLE customer_data (
    id INT,
    profile JSON
);

INSERT INTO customer_data VALUES
    (1, '{"name": "Alice", "age": 30, "city": "New York"}'),
    (2, '{"name": "Bob", "age": 25, "city": "Los Angeles"}'),
    (3, '{"name": "Charlie", "age": 35, "city": "Chicago"}');
```

Este ejemplo extrae campos específicos de los datos JSON:

```sql
SELECT
    id,
    jq('.name', profile) AS customer_name
FROM
    customer_data;

┌─────────────────────────────────────┐
│        id       │   customer_name   │
├─────────────────┼───────────────────┤
│               1 │ "Alice"           │
│               2 │ "Bob"             │
│               3 │ "Charlie"         │
└─────────────────────────────────────┘
```

Este ejemplo selecciona el ID de usuario y la edad incrementada en 1 para cada usuario:

```sql
SELECT
    id,
    jq('.age + 1', profile) AS updated_age
FROM
    customer_data;

┌─────────────────────────────────────┐
│        id       │    updated_age    │
├─────────────────┼───────────────────┤
│               1 │ 31                │
│               2 │ 26                │
│               3 │ 36                │
└─────────────────────────────────────┘
```

Este ejemplo convierte los nombres de ciudad a mayúsculas:

```sql
SELECT
    id,
    jq('.city | ascii_upcase', profile) AS city_uppercase
FROM
    customer_data;

┌─────────────────────────────────────┐
│        id       │   city_uppercase  │
├─────────────────┼───────────────────┤
│               1 │ "NEW YORK"        │
│               2 │ "LOS ANGELES"     │
│               3 │ "CHICAGO"         │
└─────────────────────────────────────┘
```
