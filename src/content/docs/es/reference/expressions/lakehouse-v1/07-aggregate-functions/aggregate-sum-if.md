---
title: SUM_IF (Lakehouse v1)
description: "SUM_IF: el sufijo -If se puede añadir al nombre de cualquier función de agregado."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-sum-if.md
---

El sufijo -If se puede añadir al nombre de cualquier función de agregado. En ese caso, la función de agregado acepta un argumento adicional: una condición.

## Sintaxis de Analyze

```python
func.sum_if(<column>, <cond>)
```

## Ejemplos de Analyze

```python
func.sum_if(table.amount, table.status=='Completed').alias('total_amount_completed')

| total_amount_completed |
|------------------------|
|         270.0          |
```

## Sintaxis de SQL

```sql
SUM_IF(<column>, <cond>)
```

## Ejemplos de SQL

**Cree una tabla e inserte datos de ejemplo**
```sql
CREATE TABLE order_data (
  id INT,
  customer_id INT,
  amount FLOAT,
  status VARCHAR
);

INSERT INTO order_data (id, customer_id, amount, status)
VALUES (1, 1, 100, 'Completed'),
       (2, 2, 50, 'Completed'),
       (3, 3, 80, 'Cancelled'),
       (4, 4, 120, 'Completed'),
       (5, 5, 75, 'Cancelled');
```

**Consulta de demostración: calcular el importe total de los pedidos completados**
```sql
SELECT SUM_IF(amount, status = 'Completed') AS total_amount_completed
FROM order_data;
```

**Resultado**
```sql
| total_amount_completed |
|------------------------|
|         270.0          |
```
