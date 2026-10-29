---
title: CUME_DIST (Lakehouse v1)
description: CUME_DIST — 値の集合における、指定した値の累積分布を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/cume-dist.md
---

値の集合における、指定した値の累積分布を返します。指定した値以下の値を持つ行の数を、行の総数で割った割合を計算します。ご注意: 結果の値は 0 から 1 の範囲（両端を含む）になります。

関連項目: [PERCENT_RANK](../percent-rank/)

## Analyzeの構文

```python
func.cume_dist().over(partition_by=[<columns>], order_by=[<columns>])
```

## Analyzeの例

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

## SQLの構文

```sql
CUME_DIST() OVER (
	PARTITION BY expr, ...
	ORDER BY expr [ASC | DESC], ...
)
```

## SQLの例

この例は、CUME_DIST() ウィンドウ関数を使用して、学生の名前、スコア、成績、および各成績内の累積分布の値（cume_dist_val）を取得します。

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
