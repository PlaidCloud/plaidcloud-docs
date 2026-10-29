---
title: MAX_IF (Lakehouse v1)
description: MAX_IF — 接尾辞 _IF は、任意の集計関数の名前に付加できます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-max-if.md
---

接尾辞 `_IF` は、任意の集計関数の名前に付加できます。この場合、集計関数は追加の引数として条件を受け取ります。

## Analyzeの構文

```python
func.max_if(<column>, <cond>)
```

## Analyzeの例

```python
func.max_if(table.revenue, table.salesperson_id==1).alias('max_revenue_salesperson_1')

| max_revenue_salesperson_1 |
|---------------------------|
|           3000            |
```

## SQLの構文

```sql
MAX_IF(<column>, <cond>)
```

## SQLの例

**テーブルの作成とサンプルデータの挿入**
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

**クエリのデモ: ID が 1 の営業担当者の最大売上を求める**

```sql
SELECT MAX_IF(revenue, salesperson_id = 1) AS max_revenue_salesperson_1
FROM sales;
```

**結果**
```sql
| max_revenue_salesperson_1 |
|---------------------------|
|           3000            |
```
