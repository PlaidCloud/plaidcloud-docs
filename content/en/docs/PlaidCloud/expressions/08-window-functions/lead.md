---
title: LEAD
---

LEAD allows you to access the value of a column from a subsequent row within the same result set. It is typically used to retrieve the value of a column in the next row, based on a specified ordering.

See also: [LAG](../lag)

## Analyze Syntax

```python
func.lead(<expr>, <offset>).over(partition_by=[<columns>], order_by=[<columns>])
```

## Analyze Examples
```python
table.product_name, table.sale_amount, func.lead(table.sale_amount, 1).over(partition_by=table.product_name, order_by=table.sale_id).alias('next_sale_amount')

product_name | sale_amount | next_sale_amount
----------------------------------------------
Product A    | 1000.00     | 1500.00
Product A    | 1500.00     | 2000.00
Product A    | 2000.00     | NULL
Product B    | 500.00      | 800.00
Product B    | 800.00      | 1200.00
Product B    | 1200.00     | NULL
```

## SQL Syntax

```sql
LEAD(expression [, offset [, default]]) OVER (PARTITION BY partition_expression ORDER BY sort_expression)
```

- *offset*: Specifies the number of rows ahead (LEAD) or behind (LAG) the current row within the partition to retrieve the value from. Defaults to 1.
> Note that setting a negative offset has the same effect as using the [LAG](lag) function.

- *default*: Specifies a value to be returned if the LEAD or LAG function encounters a situation where there is no value available due to the offset exceeding the partition's boundaries. Defaults to NULL.

## SQL Examples

```sql
CREATE TABLE sales (
  sale_id INT,
  product_name VARCHAR(50),
  sale_amount DECIMAL(10, 2)
);

INSERT INTO sales (sale_id, product_name, sale_amount)
VALUES (1, 'Product A', 1000.00),
       (2, 'Product A', 1500.00),
       (3, 'Product A', 2000.00),
       (4, 'Product B', 500.00),
       (5, 'Product B', 800.00),
       (6, 'Product B', 1200.00);

SELECT product_name, sale_amount, LEAD(sale_amount) OVER (PARTITION BY product_name ORDER BY sale_id) AS next_sale_amount
FROM sales;

product_name | sale_amount | next_sale_amount
----------------------------------------------
Product A    | 1000.00     | 1500.00
Product A    | 1500.00     | 2000.00
Product A    | 2000.00     | NULL
Product B    | 500.00      | 800.00
Product B    | 800.00      | 1200.00
Product B    | 1200.00     | NULL

-- The following statements return the same result.
SELECT product_name, sale_amount, LEAD(sale_amount, -1) OVER (PARTITION BY product_name ORDER BY sale_id) AS previous_sale_amount
FROM sales;

SELECT product_name, sale_amount, LAG(sale_amount) OVER (PARTITION BY product_name ORDER BY sale_id) AS previous_sale_amount
FROM sales;

product_name|sale_amount|previous_sale_amount|
------------+-----------+--------------------+
Product A   |    1000.00|                    |
Product A   |    1500.00|             1000.00|
Product A   |    2000.00|             1500.00|
Product B   |     500.00|                    |
Product B   |     800.00|              500.00|
Product B   |    1200.00|              800.00|
```