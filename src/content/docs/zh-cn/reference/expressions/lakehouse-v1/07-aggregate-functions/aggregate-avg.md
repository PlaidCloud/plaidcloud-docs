---
title: AVG (Lakehouse v1)
description: AVG：返回表达式的平均值，忽略 NULL 值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-avg.md
---

聚合函数。

AVG() 函数返回表达式的平均值。

**备注：** 不计入 NULL 值。


## Analyze 语法

```python
func.avg(<column>)
```

## Analyze 示例

```python
func.avg(table.price).alias('avg_price')

| avg_price |
| --------- |
| 20.4      |
```

## SQL 语法

```sql
AVG(<expr>)
```

## 参数

| 参数 | 说明 |
|-----------|--------------------------|
| `<expr>`  | 任意数值表达式 |

## 返回类型

double

## SQL 示例

**创建表并插入示例数据**

创建一个名为 "sales" 的表并插入一些示例数据：
```sql
CREATE TABLE sales (
  id INTEGER,
  product VARCHAR(50),
  price FLOAT
);

INSERT INTO sales (id, product, price)
VALUES (1, 'Product A', 10.5),
       (2, 'Product B', 20.75),
       (3, 'Product C', 30.0),
       (4, 'Product D', 15.25),
       (5, 'Product E', 25.5);
```

**查询：使用 AVG() 函数**

现在使用 AVG() 函数查找 "sales" 表中所有产品的平均价格：
```sql
SELECT AVG(price) AS avg_price
FROM sales;
```

结果应如下所示：
```sql
| avg_price |
| --------- |
| 20.4      |
```
