---
title: LAG (Lakehouse v1)
description: LAG — LAG permite aceder ao valor de uma coluna de uma linha anterior no mesmo resultado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/lag.md
---

LAG permite aceder ao valor de uma coluna de uma linha anterior no mesmo conjunto de resultados. É normalmente utilizada para obter o valor de uma coluna na linha anterior, com base numa ordenação especificada.

Consulte também: [LEAD](../lead)

## Sintaxe do Analyze

```python
func.lag(<expr>, <offset>).over(partition_by=[<columns>], order_by=[<columns>])
```

## Exemplos do Analyze

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

## Sintaxe SQL

```sql
LAG(expression [, offset [, default]]) OVER (PARTITION BY partition_expression ORDER BY sort_expression)
```

- *offset*: especifica o número de linhas à frente (LEAD) ou atrás (LAG) da linha atual, dentro da partição, de onde obter o valor. O valor predefinido é 1.
> Tenha em atenção que definir um deslocamento negativo tem o mesmo efeito que utilizar a função [LEAD](../lead).

- *default*: especifica um valor a devolver se a função LEAD ou LAG encontrar uma situação em que não existe nenhum valor disponível porque o deslocamento excede os limites da partição. O valor predefinido é NULL.

## Exemplos de SQL

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
