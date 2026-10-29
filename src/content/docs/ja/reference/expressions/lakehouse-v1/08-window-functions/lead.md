---
title: LEAD（Lakehouse v1）
description: LEAD — 同じ結果セット内の後続の行から列の値を取得できます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/lead.md
---

LEADを使用すると、同じ結果セット内の後続の行から列の値を取得できます。通常は、指定した順序に基づいて、次の行の列の値を取得するために使用します。

関連項目: [LAG](../lag)

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

- *offset*: パーティション内で、現在の行から何行先（LEAD）または何行前（LAG）の行から値を取得するかを指定します。デフォルトは1です。
> 負のオフセットを指定すると、[LAG](../lag)関数を使用した場合と同じ結果になります。

- *default*: オフセットがパーティションの範囲を超えるなどして、LEAD関数またはLAG関数が取得できる値がない場合に返す値を指定します。デフォルトはNULLです。

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
