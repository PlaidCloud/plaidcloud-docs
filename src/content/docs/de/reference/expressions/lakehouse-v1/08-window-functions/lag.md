---
title: LAG (Lakehouse v1)
description: LAG – ermöglicht den Zugriff auf den Wert einer Spalte aus einer vorangehenden Zeile innerhalb desselben Ergebnisses.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/lag.md
---

LAG ermöglicht den Zugriff auf den Wert einer Spalte aus einer vorangehenden Zeile innerhalb derselben Ergebnismenge. Die Funktion wird typischerweise verwendet, um anhand einer festgelegten Sortierung den Wert einer Spalte in der vorherigen Zeile abzurufen.

Siehe auch: [LEAD](../lead)

## Analyze-Syntax

```python
func.lag(<expr>, <offset>).over(partition_by=[<columns>], order_by=[<columns>])
```

## Analyze-Beispiele

```python
table.product_name, table.sale_amount, func.lag(table.sale_amount, 1).over(partition_by=table.product_name, order_by=table.sale_id).alias('previous_sale_amount')

product_name | sale_amount | previous_sale_amount
-----------------------------------------------
Product A    | 1000.00     | NULL
Product A    | 1500.00     | 1000.00
Product A    | 2000.00     | 1500.00
Product B    | 500.00      | NULL
Product B    | 800.00      | 500.00
Product B    | 1200.00     | 800.00
```

## SQL-Syntax

```sql
LAG(expression [, offset [, default]]) OVER (PARTITION BY partition_expression ORDER BY sort_expression)
```

- *offset*: Gibt die Anzahl der Zeilen vor (LEAD) oder hinter (LAG) der aktuellen Zeile innerhalb der Partition an, aus der der Wert abgerufen wird. Standard ist 1.
> Beachten Sie, dass ein negativer Offset denselben Effekt hat wie die Verwendung der Funktion [LEAD](../lead).

- *default*: Gibt einen Wert an, der zurückgegeben wird, wenn die Funktion LEAD oder LAG auf eine Situation trifft, in der aufgrund eines Offsets außerhalb der Partitionsgrenzen kein Wert verfügbar ist. Standard ist NULL.

## SQL-Beispiele

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

SELECT product_name, sale_amount, LAG(sale_amount) OVER (PARTITION BY product_name ORDER BY sale_id) AS previous_sale_amount
FROM sales;

product_name | sale_amount | previous_sale_amount
-----------------------------------------------
Product A    | 1000.00     | NULL
Product A    | 1500.00     | 1000.00
Product A    | 2000.00     | 1500.00
Product B    | 500.00      | NULL
Product B    | 800.00      | 500.00
Product B    | 1200.00     | 800.00

-- The following statements return the same result.
SELECT product_name, sale_amount, LAG(sale_amount, -1) OVER (PARTITION BY product_name ORDER BY sale_id) AS next_sale_amount
FROM sales;

SELECT product_name, sale_amount, LEAD(sale_amount) OVER (PARTITION BY product_name ORDER BY sale_id) AS next_sale_amount
FROM sales;

product_name|sale_amount|next_sale_amount|
------------+-----------+----------------+
Product A   |    1000.00|         1500.00|
Product A   |    1500.00|         2000.00|
Product A   |    2000.00|                |
Product B   |     500.00|          800.00|
Product B   |     800.00|         1200.00|
Product B   |    1200.00|                |
```
