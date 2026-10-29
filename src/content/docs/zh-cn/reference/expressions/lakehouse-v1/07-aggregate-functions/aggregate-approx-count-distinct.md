---
title: APPROX_COUNT_DISTINCT (Lakehouse v1)
description: APPROX_COUNT_DISTINCT：使用 HyperLogLog 算法估算数据集中不同值的数量。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-approx-count-distinct.md
---

使用 [HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog) 算法估算数据集中不同值的数量。

HyperLogLog 算法以极少的内存和时间提供唯一元素数量的近似值。处理可接受估算结果的大型数据集时，可以考虑使用此函数。它以牺牲部分精度为代价，提供了一种快速高效的返回去重计数的方法。

若要获得精确的结果，请使用 [COUNT_DISTINCT](../aggregate-count-distinct)。更多说明请参阅[示例](#sql-示例)。

## Analyze 语法

```python
func.approx_count_distinct(<expr>)
```

## Analyze 示例

```python
func.approx_count_distinct(table.user_id).alias('approx_distinct_user_count')

| approx_distinct_user_count |
|----------------------------|
|             4              |
```

## SQL 语法

```sql
APPROX_COUNT_DISTINCT(<expr>)
```

## 返回类型

整数。

## SQL 示例

**创建表并插入示例数据**
```sql
CREATE TABLE user_events (
  id INT,
  user_id INT,
  event_name VARCHAR
);

INSERT INTO user_events (id, user_id, event_name)
VALUES (1, 1, 'Login'),
       (2, 2, 'Login'),
       (3, 3, 'Login'),
       (4, 1, 'Logout'),
       (5, 2, 'Logout'),
       (6, 4, 'Login'),
       (7, 1, 'Login');
```

**查询演示：估算不同用户 ID 的数量**
```sql
SELECT APPROX_COUNT_DISTINCT(user_id) AS approx_distinct_user_count
FROM user_events;
```

**结果**
```sql
| approx_distinct_user_count |
|----------------------------|
|             4              |
```
