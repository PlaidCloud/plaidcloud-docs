---
title: ANY (Lakehouse v1)
description: "ANY: devuelve el primer valor no NULL encontrado en un conjunto; el resultado es indeterminado cuando el orden de ejecución varía."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-any.md
---

Función de agregado.

La función ANY() selecciona el primer valor (no NULL) encontrado, a menos que todas las filas tengan valores NULL en esa columna. La consulta puede ejecutarse en cualquier orden, e incluso en un orden distinto cada vez, por lo que el resultado de esta función es indeterminado. Para obtener un resultado determinado, puede usar la función ‘min’ o ‘max’ en lugar de ‘any’.

## Sintaxis de Analyze

```python
func.any(<expr>)
```

## Ejemplos de Analyze

```python
func.any(table.product_name).alias('any_product_name')

| any_product_name |
|------------------|
| Laptop           |
```

## Sintaxis de SQL

```sql
ANY(<expr>)
```

## Argumentos

| Argumentos | Descripción    |
|-----------|----------------|
| `<expr>`  | Cualquier expresión |

## Tipo de valor devuelto

El primer valor (no NULL) encontrado, con el tipo del valor. Si todos los valores son NULL, el valor devuelto es NULL.

## Ejemplos de SQL

**Cree una tabla e inserte datos de ejemplo**
```sql
CREATE TABLE product_data (
  id INT,
  product_name VARCHAR NULL,
  price FLOAT NULL
);

INSERT INTO product_data (id, product_name, price)
VALUES (1, 'Laptop', 1000),
       (2, NULL, 800),
       (3, 'Keyboard', NULL),
       (4, 'Mouse', 25),
       (5, 'Monitor', 150);
```

**Consulta de demostración: obtener el primer nombre de producto no NULL encontrado**
```sql
SELECT ANY(product_name) AS any_product_name
FROM product_data;
```

**Resultado**
```sql
| any_product_name |
|------------------|
| Laptop           |
```
