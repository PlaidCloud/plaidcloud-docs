---
title: RETENTION (Lakehouse v1)
description: RETENTION：聚合函数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-retention.md
---

聚合函数

RETENTION() 函数接受 1 到 32 个 UInt8 类型的条件作为参数，这些条件表示事件是否满足某个条件。

任何条件都可以作为参数指定（与 WHERE 中的用法相同）。

除第一个条件外，其余条件两两配对适用：如果第一个和第二个条件均为真，则第二个的结果为真；如果第一个和第三个条件均为真，则第三个的结果为真，依此类推。

## Analyze 语法

```python
func.retention(<cond1> , <cond2> , ..., <cond32>)
```

## Analyze 示例

```python
table.user_id, func.retention(table.event_type=='signup', table.event_type='login', table.event_type='purchase').alias('sales_amounts')

| user_id | retention |
|---------|-----------|
|   1     | [1, 1, 0] |
|   2     | [1, 0, 1] |
|   3     | [1, 1, 0] |
```

## SQL 语法

```sql
RETENTION( <cond1> , <cond2> , ..., <cond32> );
```

## 参数

| 参数 | 说明                                 |
|-----------|---------------------------------------------|
| `<cond>`  | 返回布尔结果的表达式 |

## 返回类型

由 1 或 0 组成的数组。

## SQL 示例

**创建表并插入示例数据**
```sql
CREATE TABLE user_events (
  id INT,
  user_id INT,
  event_date DATE,
  event_type VARCHAR
);

INSERT INTO user_events (id, user_id, event_date, event_type)
VALUES (1, 1, '2022-01-01', 'signup'),
       (2, 1, '2022-01-02', 'login'),
       (3, 2, '2022-01-01', 'signup'),
       (4, 2, '2022-01-03', 'purchase'),
       (5, 3, '2022-01-01', 'signup'),
       (6, 3, '2022-01-02', 'login');
```

**查询演示：基于注册、登录和购买事件计算用户留存**
```sql
SELECT
  user_id,
  RETENTION(event_type = 'signup', event_type = 'login', event_type = 'purchase') AS retention
FROM user_events
GROUP BY user_id;
```

**结果**
```sql
| user_id | retention |
|---------|-----------|
|   1     | [1, 1, 0] |
|   2     | [1, 0, 1] |
|   3     | [1, 1, 0] |
```
