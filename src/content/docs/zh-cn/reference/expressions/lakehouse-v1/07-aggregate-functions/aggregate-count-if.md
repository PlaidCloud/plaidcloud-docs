---
title: COUNT_IF (Lakehouse v1)
description: COUNT_IF：后缀 _IF 可以附加到任何聚合函数的名称之后。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-count-if.md
---

后缀 `_IF` 可以附加到任何聚合函数的名称之后。此时，聚合函数会接受一个额外的参数，即条件。

## Analyze 语法

```python
func.count_if(<column>, <cond>)
```

## Analyze 示例

```python
func.count_if(table.status, table.status=='Completed').alias('completed_orders')

| completed_orders |
|------------------|
|        3         |
```

## SQL 示例
```sql
COUNT_IF(<column>, <cond>)
```

## SQL 示例

**创建表并插入示例数据**
```sql
CREATE TABLE orders (
  id INT,
  customer_id INT,
  status VARCHAR,
  total FLOAT
);

INSERT INTO orders (id, customer_id, status, total)
VALUES (1, 1, 'completed', 100),
       (2, 2, 'completed', 200),
       (3, 1, 'pending', 150),
       (4, 3, 'completed', 250),
       (5, 2, 'pending', 300);
```

**查询演示：统计已完成的订单**
```sql
SELECT COUNT_IF(status, status = 'completed') AS completed_orders
FROM orders;
```

**结果**
```sql
| completed_orders |
|------------------|
|        3         |
```
