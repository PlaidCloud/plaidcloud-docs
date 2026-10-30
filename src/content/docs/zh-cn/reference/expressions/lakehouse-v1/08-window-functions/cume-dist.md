---
title: CUME_DIST (Lakehouse v1)
description: CUME_DIST：返回给定值在一组值中的累积分布。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/cume-dist.md
---

返回给定值在一组值中的累积分布。它计算值小于或等于指定值的行所占的比例，即此类行数除以总行数。请注意，结果值介于 0 和 1 之间（含 0 和 1）。

另请参阅：[PERCENT_RANK](../percent-rank/)

## Analyze 语法

```python
func.cume_dist().over(partition_by=[<columns>], order_by=[<columns>])
```

## Analyze 示例

```python
table.name, table.score, table.grade, func.cume_dist().over(partition_by=[table.grade], order_by=table.score).alias('cume_dist_val')

name    |score|grade|cume_dist_val|
--------+-----+-----+-------------+
Smith   |   81|A    |         0.25|
Davies  |   84|A    |          0.5|
Evans   |   87|A    |         0.75|
Johnson |  100|A    |          1.0|
Taylor  |   62|B    |          0.5|
Brown   |   62|B    |          0.5|
Wilson  |   72|B    |          1.0|
Thomas  |   72|B    |          1.0|
Jones   |   55|C    |          1.0|
Williams|   55|C    |          1.0|
```

## SQL 语法

```sql
CUME_DIST() OVER (
	PARTITION BY expr, ...
	ORDER BY expr [ASC | DESC], ...
)
```

## SQL 示例

此示例使用 CUME_DIST() 窗口函数检索学生的姓名、分数、等级，以及每个等级内的累积分布值（cume_dist_val）。

```sql
CREATE TABLE students (
    name VARCHAR(20),
    score INT NOT NULL,
    grade CHAR(1) NOT NULL
);

INSERT INTO students (name, score, grade)
VALUES
    ('Smith', 81, 'A'),
    ('Jones', 55, 'C'),
    ('Williams', 55, 'C'),
    ('Taylor', 62, 'B'),
    ('Brown', 62, 'B'),
    ('Davies', 84, 'A'),
    ('Evans', 87, 'A'),
    ('Wilson', 72, 'B'),
    ('Thomas', 72, 'B'),
    ('Johnson', 100, 'A');

SELECT
    name,
    score,
    grade,
    CUME_DIST() OVER (PARTITION BY grade ORDER BY score) AS cume_dist_val
FROM
    students;

name    |score|grade|cume_dist_val|
--------+-----+-----+-------------+
Smith   |   81|A    |         0.25|
Davies  |   84|A    |          0.5|
Evans   |   87|A    |         0.75|
Johnson |  100|A    |          1.0|
Taylor  |   62|B    |          0.5|
Brown   |   62|B    |          0.5|
Wilson  |   72|B    |          1.0|
Thomas  |   72|B    |          1.0|
Jones   |   55|C    |          1.0|
Williams|   55|C    |          1.0|
```
