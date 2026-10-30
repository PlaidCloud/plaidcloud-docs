---
title: NTILE（Lakehouse v1）
description: NTILE — 将排序后的结果集划分为指定数量的桶（分组）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/ntile.md
---

将排序后的结果集划分为指定数量的桶（分组）。该函数将排序后的行均匀分配到这些桶中，并为每一行分配一个桶编号。NTILE 函数通常与 ORDER BY 子句配合使用来对结果排序。

请注意，NTILE 函数根据行的排序顺序将行均匀分配到各个桶中，并确保每个桶中的行数尽可能相等。如果行数无法被桶数整除，部分桶会比其他桶多出一行。

## Analyze 语法

```python
func.ntile(<n>).over(partition_by=[<columns>], order_by=[<columns>])
```

## Analyze 示例

```python
table.name, table.score, table.grade, func.ntile(3).over(partition_by=[table.grade], order_by=table.score).alias('bucket')

name    |score|grade|bucket|
--------+-----+-----+------+
Johnson |  100|A    |     1|
Evans   |   87|A    |     1|
Davies  |   84|A    |     2|
Smith   |   81|A    |     3|
Wilson  |   72|B    |     1|
Thomas  |   72|B    |     1|
Taylor  |   62|B    |     2|
Brown   |   62|B    |     3|
Jones   |   55|C    |     1|
Williams|   55|C    |     2|
```

## SQL 语法

```sql
NTILE(n) OVER (
	PARTITION BY expr, ...
	ORDER BY expr [ASC | DESC], ...
)
```

## SQL 示例

此示例使用 NTILE() 窗口函数检索学生的姓名、分数和成绩等级，并根据分数将其分配到各成绩等级内的桶中。

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
    ntile(3) OVER (PARTITION BY grade ORDER BY score DESC) AS bucket
FROM
    students;

name    |score|grade|bucket|
--------+-----+-----+------+
Johnson |  100|A    |     1|
Evans   |   87|A    |     1|
Davies  |   84|A    |     2|
Smith   |   81|A    |     3|
Wilson  |   72|B    |     1|
Thomas  |   72|B    |     1|
Taylor  |   62|B    |     2|
Brown   |   62|B    |     3|
Jones   |   55|C    |     1|
Williams|   55|C    |     2|
```
