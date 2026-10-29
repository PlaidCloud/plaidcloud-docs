---
title: PERCENT_RANK（Lakehouse v1）
description: PERCENT_RANK — 値の集合の中での、指定した値の相対順位を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/percent-rank.md
---

値の集合の中での、指定した値の相対順位を返します。結果の値は0から1の範囲（0と1を含む）になります。ご注意: どの集合でも、最初の行のPERCENT_RANKは0です。

関連項目: [CUME_DIST](../cume-dist)

## Analyze Syntax

```python
func.percent_rank().over(partition_by=[<columns>], order_by=[<columns>])
```

## Analyze Examples

```python
table.name, table.score, table.grade, func.percent_rank().over(partition_by=[table.grade], order_by=table.score).alias('percent_rank')

name    |score|grade|percent_rank      |
--------+-----+-----+------------------+
Smith   |   81|A    |               0.0|
Davies  |   84|A    |0.3333333333333333|
Evans   |   87|A    |0.6666666666666666|
Johnson |  100|A    |               1.0|
Taylor  |   62|B    |               0.0|
Brown   |   62|B    |               0.0|
Wilson  |   72|B    |0.6666666666666666|
Thomas  |   72|B    |0.6666666666666666|
Jones   |   55|C    |               0.0|
Williams|   55|C    |               0.0|
```

## SQL Syntax

```sql
PERCENT_RANK() OVER (
	PARTITION BY expr, ...
	ORDER BY expr [ASC | DESC], ...
)
```

## SQL Examples

この例では、PERCENT_RANK()ウィンドウ関数を使用して、生徒の名前、スコア、成績、および各成績内でのパーセンタイル順位（percent_rank）を取得します。

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
    PERCENT_RANK() OVER (PARTITION BY grade ORDER BY score) AS percent_rank
FROM
    students;

name    |score|grade|percent_rank      |
--------+-----+-----+------------------+
Smith   |   81|A    |               0.0|
Davies  |   84|A    |0.3333333333333333|
Evans   |   87|A    |0.6666666666666666|
Johnson |  100|A    |               1.0|
Taylor  |   62|B    |               0.0|
Brown   |   62|B    |               0.0|
Wilson  |   72|B    |0.6666666666666666|
Thomas  |   72|B    |0.6666666666666666|
Jones   |   55|C    |               0.0|
Williams|   55|C    |               0.0|
```
