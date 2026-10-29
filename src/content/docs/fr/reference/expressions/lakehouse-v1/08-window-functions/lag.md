---
title: LAG (Lakehouse v1)
description: "LAG : LAG permet d'accéder à la valeur d'une colonne d'une ligne précédente dans le même résultat."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/lag.md
---

LAG permet d'accéder à la valeur d'une colonne d'une ligne précédente dans le même jeu de résultats. Elle sert généralement à récupérer la valeur d'une colonne de la ligne précédente, selon un ordre spécifié.

Voir aussi : [LEAD](../lead)

## Syntaxe Analyze

```python
func.lag(<expr>, <offset>).over(partition_by=[<columns>], order_by=[<columns>])
```

## Exemples Analyze

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

## Syntaxe SQL

```sql
LAG(expression [, offset [, default]]) OVER (PARTITION BY partition_expression ORDER BY sort_expression)
```

- *offset* : indique le nombre de lignes après (LEAD) ou avant (LAG) la ligne courante, au sein de la partition, d'où récupérer la valeur. La valeur par défaut est 1.
> Remarque : définir un décalage négatif produit le même effet que l'utilisation de la fonction [LEAD](../lead).

- *default* : indique la valeur à renvoyer lorsque la fonction LEAD ou LAG ne trouve aucune valeur disponible parce que le décalage dépasse les limites de la partition. La valeur par défaut est NULL.

## Exemples SQL

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
