---
title: AVG (Lakehouse v1)
description: "AVG: devuelve el valor promedio de una expresión, ignorando los valores NULL."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-avg.md
---

Función de agregado.

La función AVG() devuelve el valor promedio de una expresión.

**Nota:** los valores NULL no se cuentan.


## Sintaxis de Analyze

```python
func.avg(<column>)
```

## Ejemplos de Analyze

```python
func.avg(table.price).alias('avg_price')

| avg_price |
| --------- |
| 20.4      |
```

## Sintaxis de SQL

```sql
AVG(<expr>)
```

## Argumentos

| Argumentos | Descripción              |
|-----------|--------------------------|
| `<expr>`  | Cualquier expresión numérica |

## Tipo de valor devuelto

double

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

**Consulta: uso de la función AVG()**

Ahora use la función AVG() para encontrar el precio promedio de todos los productos de la tabla "sales":
```sql
SELECT AVG(price) AS avg_price
FROM sales;
```

El resultado debería tener este aspecto:
```sql
| avg_price |
| --------- |
| 20.4      |
```
