---
title: SUM_IF (Lakehouse v1)
description: SUM_IF：后缀 -If 可以附加到任何聚合函数的名称之后。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-sum-if.md
---

后缀 -If 可以附加到任何聚合函数的名称之后。此时，聚合函数会接受一个额外的参数，即条件。

## Analyze 语法

```python
func.sum_if(<column>, <cond>)
```

## Analyze 示例

```python
func.sum_if(table.amount, table.status=='Completed').alias('total_amount_completed')

| total_amount_completed |
|------------------------|
|         270.0          |
```

## SQL 语法

```sql
SUM_IF(<column>, <cond>)
```

## SQL 示例

**创建表并插入示例数据**
```sql
CREATE TABLE order_data (
  id INT,
  customer_id INT,
  amount FLOAT,
  status VARCHAR
);

INSERT INTO order_data (id, customer_id, amount, status)
VALUES (1, 1, 100, 'Completed'),
       (2, 2, 50, 'Completed'),
       (3, 3, 80, 'Cancelled'),
       (4, 4, 120, 'Completed'),
       (5, 5, 75, 'Cancelled');
```

**查询演示：计算已完成订单的总金额**
```sql
SELECT SUM_IF(amount, status = 'Completed') AS total_amount_completed
FROM order_data;
```

**结果**
```sql
| total_amount_completed |
|------------------------|
|         270.0          |
```
