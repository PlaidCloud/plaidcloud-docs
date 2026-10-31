---
title: COVAR_POP (Lakehouse v1)
description: COVAR_POP — COVAR_POP は、数値ペアの集合の母共分散を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-covar-pop.md
---

COVAR_POP は、数値ペアの集合の母共分散を返します。

## Analyzeの構文

```python
func.covar_pop(<expr1>, <expr2>)
```

## Analyzeの例

```python
func.covar_pop(table.units_sold, table.revenue).alias('covar_pop_units_revenue')

| covar_pop_units_revenue |
|-------------------------|
|        20000.0          |
```

## SQLの構文

```sql
COVAR_POP(<expr1>, <expr2>)
```

## 引数

| 引数 |        説明       |
|-----------| ------------------------ |
| `<expr1>` | 任意の数値式 |
| `<expr2>` | 任意の数値式 |

## 戻り値の型

float64

## SQLの例

**テーブルの作成とサンプルデータの挿入**
```sql
CREATE TABLE product_sales (
  id INT,
  product_id INT,
  units_sold INT,
  revenue FLOAT
);

INSERT INTO product_sales (id, product_id, units_sold, revenue)
VALUES (1, 1, 10, 1000),
       (2, 2, 20, 2000),
       (3, 3, 30, 3000),
       (4, 4, 40, 4000),
       (5, 5, 50, 5000);
```

**クエリのデモ: 販売数量と売上の母共分散を計算する**

```sql
SELECT COVAR_POP(units_sold, revenue) AS covar_pop_units_revenue
FROM product_sales;
```

**結果**
```sql
| covar_pop_units_revenue |
|-------------------------|
|        20000.0          |
```
