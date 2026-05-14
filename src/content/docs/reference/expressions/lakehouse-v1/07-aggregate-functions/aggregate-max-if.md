---
title: MAX_IF
description: "Learn how to use the MAX_IF aggregate function in PlaidCloud Lakehouse. The suffix _IF can be appended to the name of any aggregate function."
---

The suffix `_IF` can be appended to the name of any aggregate function. In this case, the aggregate function accepts an extra argument – a condition.

## Analyze Syntax

```python
func.max_if(<column>, <cond>)
```

## Analyze Examples

```python
func.max_if(table.revenue, table.salesperson_id==1).alias('max_revenue_salesperson_1')

| max_revenue_salesperson_1 |
|---------------------------|
|           3000            |
```

## SQL Example

```sql
MAX_IF(<column>, <cond>)
```

## SQL Examples

**Create a Table and Insert Sample Data**
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

**Query Demo: Find Maximum Revenue for Salesperson with ID 1**

```sql
SELECT MAX_IF(revenue, salesperson_id = 1) AS max_revenue_salesperson_1
FROM sales;
```

**Result**
```sql
| max_revenue_salesperson_1 |
|---------------------------|
|           3000            |
```
