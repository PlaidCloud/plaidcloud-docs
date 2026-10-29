---
title: NTILE（Lakehouse v1）
description: NTILE — ソートされた結果セットを、指定した数のバケット（グループ）に分割します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/ntile.md
---

ソートされた結果セットを、指定した数のバケット（グループ）に分割します。ソートされた行をこれらのバケットに均等に振り分け、各行にバケット番号を割り当てます。NTILE関数は通常、ORDER BY句と組み合わせて結果をソートします。

ご注意: NTILE関数は、行のソート順に基づいて行をバケットに均等に振り分け、各バケットの行数ができるだけ等しくなるようにします。行をバケットに均等に振り分けられない場合は、一部のバケットの行数が他のバケットより1行多くなることがあります。

## Analyze Syntax

```python
func.ntile(<n>).over(partition_by=[<columns>], order_by=[<columns>])
```

## Analyze Examples

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

## SQL Syntax

```sql
NTILE(n) OVER (
	PARTITION BY expr, ...
	ORDER BY expr [ASC | DESC], ...
)
```

## SQL Examples

この例では、NTILE()ウィンドウ関数を使用して、生徒の名前、スコア、成績を取得し、各成績内のスコアに基づいてバケットに割り当てます。

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
