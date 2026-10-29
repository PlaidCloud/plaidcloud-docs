---
title: ARRAY_AGG (Lakehouse v1)
description: ARRAY_AGG：ARRAY_AGG 函数（别名为 LIST）转换所有值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-array-agg.md
---

ARRAY_AGG 函数（别名为 LIST）将查询结果中某一列的所有值（包括 NULL）转换为一个数组。

## Analyze 语法

```python
func.array_agg(<expr>)
```

## Analyze 示例

```python
table.movie_title, func.array_agg(table.rating).alias('ratings')

| movie_title |  ratings   |
|-------------|------------|
| Inception   | [5, 4, 5]  |
```

## SQL 语法

```sql
ARRAY_AGG(<expr>)

LIST(<expr>)
```

## 参数

| 参数 | 说明 |
|-----------| -------------- |
| `<expr>`  | 任意表达式 |

## 返回类型

返回一个数组，其元素与原始数据的类型相同。

## SQL 示例

此示例演示如何使用 ARRAY_AGG 函数以便捷的数组格式聚合并呈现数据：

```sql
-- Create a table and insert sample data
CREATE TABLE movie_ratings (
  id INT,
  movie_title VARCHAR,
  user_id INT,
  rating INT
);

INSERT INTO movie_ratings (id, movie_title, user_id, rating)
VALUES (1, 'Inception', 1, 5),
       (2, 'Inception', 2, 4),
       (3, 'Inception', 3, 5),
       (4, 'Interstellar', 1, 4),
       (5, 'Interstellar', 2, 3);

-- List all ratings for Inception in an array
SELECT movie_title, ARRAY_AGG(rating) AS ratings
FROM movie_ratings
WHERE movie_title = 'Inception'
GROUP BY movie_title;

| movie_title |  ratings   |
|-------------|------------|
| Inception   | [5, 4, 5]  |
```
