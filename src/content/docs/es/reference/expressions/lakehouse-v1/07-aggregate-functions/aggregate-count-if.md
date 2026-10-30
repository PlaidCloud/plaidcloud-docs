---
title: COUNT_IF (Lakehouse v1)
description: "COUNT_IF: el sufijo _IF se puede añadir al nombre de cualquier función de agregado."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-count-if.md
---

El sufijo `_IF` se puede añadir al nombre de cualquier función de agregado. En ese caso, la función de agregado acepta un argumento adicional: una condición.

## Sintaxis de Analyze

```python
func.count_if(<column>, <cond>)
```

## Ejemplos de Analyze

```python
func.count_if(table.status, table.status=='Completed').alias('completed_orders')

| completed_orders |
|------------------|
|        3         |
```

## Ejemplo de SQL
```sql
COUNT_IF(<column>, <cond>)
```

## Ejemplos de SQL

**Cree una tabla e inserte datos de ejemplo**
```sql
CREATE TABLE orders (
  id INT,
  customer_id INT,
  status VARCHAR,
  total FLOAT
);

INSERT INTO orders (id, customer_id, status, total)
VALUES (1, 1, 'completed', 100),
       (2, 2, 'completed', 200),
       (3, 1, 'pending', 150),
       (4, 3, 'completed', 250),
       (5, 2, 'pending', 300);
```

**Consulta de demostración: contar los pedidos completados**
```sql
SELECT COUNT_IF(status, status = 'completed') AS completed_orders
FROM orders;
```

**Resultado**
```sql
| completed_orders |
|------------------|
|        3         |
```
