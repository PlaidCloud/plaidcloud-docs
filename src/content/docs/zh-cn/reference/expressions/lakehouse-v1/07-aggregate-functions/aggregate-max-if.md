---
title: MAX_IF (Lakehouse v1)
description: MAX_IF：后缀 _IF 可以附加到任何聚合函数的名称之后。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-max-if.md
---

后缀 `_IF` 可以附加到任何聚合函数的名称之后。此时，聚合函数会接受一个额外的参数，即条件。

## Analyze 语法

```python
func.max_if(<column>, <cond>)
```

## Analyze 示例

```python
func.max_if(table.revenue, table.salesperson_id==1).alias('max_revenue_salesperson_1')

| max_revenue_salesperson_1 |
|---------------------------|
|           3000            |
```

## SQL 示例

```sql
MAX_IF(<column>, <cond>)
```

## SQL 示例

**创建表并插入示例数据**
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

**查询演示：查找 ID 为 1 的销售人员的最大收入**

```sql
SELECT MAX_IF(revenue, salesperson_id = 1) AS max_revenue_salesperson_1
FROM sales;
```

**结果**
```sql
| max_revenue_salesperson_1 |
|---------------------------|
|           3000            |
```
