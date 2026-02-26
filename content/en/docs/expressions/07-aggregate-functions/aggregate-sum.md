---
title: SUM
---

Aggregate function.

The SUM() function calculates the sum of a set of values.

{{< caution >}}
NULL values are not counted.
{{< /caution >}}


## Analyze Syntax

```python
func.sum(<column>)
```

## Analyze Examples
```python
func.sum(table.quantity).alias('total_quantity_sold')

| total_quantity_sold |
|---------------------|
|         41          |
```

## SQL Syntax

```
SUM(<expr>)
```

## Arguments

| Arguments | Description              |
|-----------|--------------------------|
| `<expr>`  | Any numerical expression |

## Return Type

A double if the input type is double, otherwise integer.

## SQL Examples

**Create a Table and Insert Sample Data**
```sql
CREATE TABLE sales_data (
  id INT,
  product_id INT,
  quantity INT
);

INSERT INTO sales_data (id, product_id, quantity)
VALUES (1, 1, 10),
       (2, 2, 5),
       (3, 3, 8),
       (4, 4, 3),
       (5, 5, 15);
```

**Query Demo: Calculate the Total Quantity of Products Sold**
```sql
SELECT SUM(quantity) AS total_quantity_sold
FROM sales_data;
```

**Result**
```sql
| total_quantity_sold |
|---------------------|
|         41          |
```
