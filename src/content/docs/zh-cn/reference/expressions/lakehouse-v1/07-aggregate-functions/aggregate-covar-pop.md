---
title: COVAR_POP (Lakehouse v1)
description: COVAR_POP：返回一组数值对的总体协方差。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-covar-pop.md
---

COVAR_POP 返回一组数值对的总体协方差。

## Analyze 语法

```python
func.covar_pop(<expr1>, <expr2>)
```

## Analyze 示例

```python
func.covar_pop(table.units_sold, table.revenue).alias('covar_pop_units_revenue')

| covar_pop_units_revenue |
|-------------------------|
|        20000.0          |
```

## SQL 语法

```sql
COVAR_POP(<expr1>, <expr2>)
```

## 参数

| 参数 |        说明       |
|-----------| ------------------------ |
| `<expr1>` | 任意数值表达式 |
| `<expr2>` | 任意数值表达式 |

## 返回类型

float64

## SQL 示例

**创建表并插入示例数据**
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

**查询演示：计算销量与收入之间的总体协方差**

```sql
SELECT COVAR_POP(units_sold, revenue) AS covar_pop_units_revenue
FROM product_sales;
```

**结果**
```sql
| covar_pop_units_revenue |
|-------------------------|
|        20000.0          |
```
