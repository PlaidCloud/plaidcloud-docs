---
title: SUM_IF
---

The suffix -If can be appended to the name of any aggregate function. In this case, the aggregate function accepts an extra argument – a condition.

## Analyze Syntax

```python
func.sum_if(<column>, <cond>)
```

## Analyze Examples
```python
func.sum_if(table.amount, table.status=='Completed').alias('total_amount_completed')

| total_amount_completed |
|------------------------|
|         270.0          |
```

## SQL Syntax

```
SUM_IF(<column>, <cond>)
```

## SQL Examples

**Create a Table and Insert Sample Data**
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

**Query Demo: Calculate the Total Amount of Completed Orders**
```sql
SELECT SUM_IF(amount, status = 'Completed') AS total_amount_completed
FROM order_data;
```

**Result**
```sql
| total_amount_completed |
|------------------------|
|         270.0          |
```