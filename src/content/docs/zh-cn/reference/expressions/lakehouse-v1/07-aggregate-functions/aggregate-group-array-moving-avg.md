---
title: GROUP_ARRAY_MOVING_AVG (Lakehouse v1)
description: GROUP_ARRAY_MOVING_AVG：GROUP_ARRAY_MOVING_AVG 函数计算输入值的移动平均值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-group-array-moving-avg.md
---

GROUP_ARRAY_MOVING_AVG 函数计算输入值的移动平均值。该函数可以接受窗口大小作为参数。如果未指定，则窗口大小等于输入值的数量。

## Analyze 语法

```python
func.group_array_moving_avg(<expr1>)
```

## Analyze 示例

```python
table.user_id, func.group_array_moving_avg(table.request_num).alias('avg_request_num')

| user_id | avg_request_num  |
|---------|------------------|
|       1 | [5.0,11.5,21.5]  |
|       3 | [10.0,22.5,35.0] |
|       2 | [7.5,18.0,31.0]  |
```

## SQL 语法

```sql
GROUP_ARRAY_MOVING_AVG(<expr>)

GROUP_ARRAY_MOVING_AVG(<window_size>)(<expr>)
```

## 参数

| 参数        | 说明              |
|------------------| ------------------------ |
| `<window_size>`  | 任意数值表达式 |
| `<expr>`         | 任意数值表达式 |

## 返回类型

返回一个数组，其元素为 double 或 decimal，具体取决于源数据类型。

## SQL 示例

```sql
-- Create a table and insert sample data
CREATE TABLE hits (
  user_id INT,
  request_num INT
);

INSERT INTO hits (user_id, request_num)
VALUES (1, 10),
       (2, 15),
       (3, 20),
       (1, 13),
       (2, 21),
       (3, 25),
       (1, 30),
       (2, 41),
       (3, 45);

SELECT user_id, GROUP_ARRAY_MOVING_AVG(2)(request_num) AS avg_request_num
FROM hits
GROUP BY user_id;

| user_id | avg_request_num  |
|---------|------------------|
|       1 | [5.0,11.5,21.5]  |
|       3 | [10.0,22.5,35.0] |
|       2 | [7.5,18.0,31.0]  |
```
