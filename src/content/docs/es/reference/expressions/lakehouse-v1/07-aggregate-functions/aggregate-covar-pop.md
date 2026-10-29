---
title: COVAR_POP (Lakehouse v1)
description: "COVAR_POP: devuelve la covarianza poblacional de un conjunto de pares de números."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-covar-pop.md
---

COVAR_POP devuelve la covarianza poblacional de un conjunto de pares de números. 

## Sintaxis de Analyze

```python
func.covar_pop(<expr1>, <expr2>)
```

## Ejemplos de Analyze

```python
func.covar_pop(table.units_sold, table.revenue).alias('covar_pop_units_revenue')

| covar_pop_units_revenue |
|-------------------------|
|        20000.0          |
```

## Sintaxis de SQL

```sql
COVAR_POP(<expr1>, <expr2>)
```

## Argumentos

| Argumentos |        Descripción       |
|-----------| ------------------------ |
| `<expr1>` | Cualquier expresión numérica |
| `<expr2>` | Cualquier expresión numérica |

## Tipo de valor devuelto

float64

## Ejemplos de SQL

**Cree una tabla e inserte datos de ejemplo**
```sql
CREATE TABLE product_sales (
  id INT,
  product_id INT,
  units_sold INT,
  revenue FLOAT
);

INSERT INTO product_sales (id, product_id, units_sold, revenue)
VALUES (1, 1, 10, 1000),
       (2, 2, 20, 2000),
       (3, 3, 30, 3000),
       (4, 4, 40, 4000),
       (5, 5, 50, 5000);
```

**Consulta de demostración: calcular la covarianza poblacional entre unidades vendidas e ingresos**

```sql
SELECT COVAR_POP(units_sold, revenue) AS covar_pop_units_revenue
FROM product_sales;
```

**Resultado**
```sql
| covar_pop_units_revenue |
|-------------------------|
|        20000.0          |
```
