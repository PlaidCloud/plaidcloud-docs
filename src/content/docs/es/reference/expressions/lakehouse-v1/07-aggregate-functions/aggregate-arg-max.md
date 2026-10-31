---
title: ARG_MAX (Lakehouse v1)
description: "ARG_MAX: calcula el valor de arg correspondiente al valor máximo de val."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-arg-max.md
---

Calcula el valor de `arg` correspondiente al valor máximo de `val`. Si hay varios valores de `arg` para los valores máximos de `val`, devuelve el primero de ellos que se encuentre.

## Sintaxis de Analyze

```python
func.arg_max(<expr>)
```

## Ejemplos de Analyze

```python
func.arg_max(table.product, table.price).alias('max_price_product')

| max_price_product |
| ----------------- |
| Product C         |
```

## Sintaxis de SQL

```sql
ARG_MAX(<arg>, <val>)
```

## Argumentos

| Argumentos | Descripción                                                                                       |
|-----------|---------------------------------------------------------------------------------------------------|
| `<arg>`   | Argumento de cualquier tipo de datos compatible con PlaidCloud Lakehouse |
| `<val>`   | Valor de cualquier tipo de datos compatible con PlaidCloud Lakehouse    |

## Tipo de valor devuelto

Valor de `arg` correspondiente al valor máximo de `val`.

 coincide con el tipo de `arg`.

## Ejemplos de SQL

**Creación de una tabla e inserción de datos de ejemplo**

Cree una tabla llamada "sales" e inserte algunos datos de ejemplo:
```sql
CREATE TABLE sales (
  id INTEGER,
  product VARCHAR(50),
  price FLOAT
);

INSERT INTO sales (id, product, price)
VALUES (1, 'Product A', 10.5),
       (2, 'Product B', 20.75),
       (3, 'Product C', 30.0),
       (4, 'Product D', 15.25),
       (5, 'Product E', 25.5);
```

**Consulta: uso de la función ARG_MAX()**

Ahora use la función ARG_MAX() para encontrar el producto con el precio máximo:
```sql
SELECT ARG_MAX(product, price) AS max_price_product
FROM sales;
```

El resultado debería tener este aspecto:
```sql
| max_price_product |
| ----------------- |
| Product C         |
```
