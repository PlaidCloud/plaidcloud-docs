---
title: LEAD (Lakehouse v1)
description: LEAD — umożliwia dostęp do wartości kolumny z następnego wiersza w tym samym zbiorze wyników.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/lead.md
---

LEAD umożliwia dostęp do wartości kolumny z kolejnego wiersza w tym samym zbiorze wyników. Zazwyczaj służy do pobrania wartości kolumny z następnego wiersza, zgodnie z określoną kolejnością.

Zobacz też: [LAG](../lag)

## Składnia Analyze

```python
func.lead(<expr>, <offset>).over(partition_by=[<columns>], order_by=[<columns>])
```

## Przykłady Analyze

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

## Składnia SQL

```sql
LEAD(expression [, offset [, default]]) OVER (PARTITION BY partition_expression ORDER BY sort_expression)
```

- *offset*: określa, o ile wierszy do przodu (LEAD) lub do tyłu (LAG) względem bieżącego wiersza w partycji należy pobrać wartość. Wartość domyślna to 1.
> Ujemna wartość offset daje ten sam efekt co użycie funkcji [LAG](../lag).

- *default*: określa wartość zwracaną, gdy funkcja LEAD lub LAG nie znajdzie wartości, ponieważ offset wykracza poza granice partycji. Wartość domyślna to NULL.

## Przykłady SQL

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
