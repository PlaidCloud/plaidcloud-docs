---
title: MAX_IF (Lakehouse v1)
description: "MAX_IF: el sufijo _IF se puede añadir al nombre de cualquier función de agregado."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-max-if.md
---

El sufijo `_IF` se puede añadir al nombre de cualquier función de agregado. En ese caso, la función de agregado acepta un argumento adicional: una condición.

## Sintaxis de Analyze

```python
func.max_if(<column>, <cond>)
```

## Ejemplos de Analyze

```python
func.max_if(table.revenue, table.salesperson_id==1).alias('max_revenue_salesperson_1')

| max_revenue_salesperson_1 |
|---------------------------|
|           3000            |
```

## Ejemplo de SQL

```sql
MAX_IF(<column>, <cond>)
```

## Ejemplos de SQL

**Cree una tabla e inserte datos de ejemplo**
```sql
CREATE TABLE sales (
  id INT,
  salesperson_id INT,
  product_id INT,
  revenue FLOAT
);

INSERT INTO sales (id, salesperson_id, product_id, revenue)
VALUES (1, 1, 1, 1000),
       (2, 1, 2, 2000),
       (3, 1, 3, 3000),
       (4, 2, 1, 1500),
       (5, 2, 2, 2500);
```

**Consulta de demostración: encontrar los ingresos máximos del vendedor con ID 1**

```sql
SELECT MAX_IF(revenue, salesperson_id = 1) AS max_revenue_salesperson_1
FROM sales;
```

**Resultado**
```sql
| max_revenue_salesperson_1 |
|---------------------------|
|           3000            |
```
