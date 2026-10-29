---
title: JSON_OBJECT_AGG (Lakehouse v1)
description: "JSON_OBJECT_AGG: convierte pares clave-valor en un objeto JSON."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-json-object-agg.md
---

Convierte pares clave-valor en un objeto JSON. Para cada fila de la entrada, genera un par clave-valor en el que la clave se obtiene de `<key_expression>` y el valor se obtiene de `<value_expression>`. Después, estos pares clave-valor se combinan en un único objeto JSON.

Consulte también: [JSON_ARRAY_AGG](../aggregate-json-array-agg)

## Sintaxis de Analyze

```python
func.json_object_agg(<key_expression>, <value_expression>)
```

## Ejemplos de Analyze
Consulte el ejemplo de SQL para obtener más información

## Sintaxis de SQL

```sql
JSON_OBJECT_AGG(<key_expression>, <value_expression>)
```

| Parámetro        | Descripción                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| key_expression   | Especifica la clave del objeto JSON. **Solo admite expresiones de cadena**. Si `key_expression` se evalúa como NULL, se omite el par clave-valor.  |
| value_expression | Especifica el valor del objeto JSON. Puede ser de cualquier tipo de datos admitido. Si `value_expression` se evalúa como NULL, se omite el par clave-valor. |

## Tipo de valor devuelto

Objeto JSON.

## Ejemplos de SQL

Este ejemplo muestra cómo se puede usar JSON_OBJECT_AGG para agregar distintos tipos de datos (como decimales, enteros, variantes JSON y matrices) en objetos JSON, con la columna b como clave de cada objeto JSON:

```sql
CREATE TABLE d (
    a DECIMAL(10, 2), 
    b STRING, 
    c INT, 
    d VARIANT, 
    e ARRAY(STRING)
);

INSERT INTO d VALUES
    (20, 'abc', NULL, '{"k":"v"}', ['a','b']),
    (10, 'de', 100, 'null', []),
    (4.23, NULL, 200, '"uvw"', ['x','y']),
    (5.99, 'xyz', 300, '[1,2,3]', ['z']);

SELECT
    json_object_agg(b, a) AS json_a,
    json_object_agg(b, c) AS json_c,
    json_object_agg(b, d) AS json_d,
    json_object_agg(b, e) AS json_e
FROM
    d;

-[ RECORD 1 ]-----------------------------------
json_a: {"abc":20.0,"de":10.0,"xyz":5.99}
json_c: {"de":100,"xyz":300}
json_d: {"abc":{"k":"v"},"de":null,"xyz":[1,2,3]}
json_e: {"abc":["a","b"],"de":[],"xyz":["z"]}
```
