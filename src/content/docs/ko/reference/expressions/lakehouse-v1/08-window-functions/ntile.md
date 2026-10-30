---
title: NTILE (Lakehouse v1)
description: NTILE — 정렬된 결과 집합을 지정한 개수의 버킷 또는 그룹으로 나눕니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/ntile.md
---

정렬된 결과 집합을 지정한 개수의 버킷 또는 그룹으로 나눕니다. 정렬된 행을 이러한 버킷에 고르게 분배하고 각 행에 버킷 번호를 할당합니다. NTILE 함수는 일반적으로 ORDER BY 절과 함께 사용하여 결과를 정렬합니다.

참고: NTILE 함수는 행의 정렬 순서에 따라 행을 버킷에 고르게 분배하며, 각 버킷의 행 수가 최대한 같도록 보장합니다. 행을 버킷에 균등하게 나눌 수 없는 경우 일부 버킷에는 다른 버킷보다 행이 하나 더 포함될 수 있습니다.

## Analyze 구문

```python
func.ntile(<n>).over(partition_by=[<columns>], order_by=[<columns>])
```

## Analyze 예제

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

## SQL 구문

```sql
NTILE(n) OVER (
	PARTITION BY expr, ...
	ORDER BY expr [ASC | DESC], ...
)
```

## SQL 예제

이 예제는 NTILE() 윈도 함수를 사용하여 학생의 이름, 점수, 등급을 조회하고 각 등급 내에서 점수에 따라 버킷에 할당합니다.

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
