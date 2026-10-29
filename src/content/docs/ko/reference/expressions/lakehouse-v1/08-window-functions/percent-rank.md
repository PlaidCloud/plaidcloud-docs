---
title: PERCENT_RANK (Lakehouse v1)
description: PERCENT_RANK — 값 집합 내에서 지정한 값의 상대 순위를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/percent-rank.md
---

값 집합 내에서 지정한 값의 상대 순위를 반환합니다. 결과 값은 0 이상 1 이하입니다. 참고: 모든 집합의 첫 번째 행은 PERCENT_RANK가 0입니다.

참고: [CUME_DIST](../cume-dist)

## Analyze 구문

```python
func.percent_rank().over(partition_by=[<columns>], order_by=[<columns>])
```

## Analyze 예제

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

## SQL 구문

```sql
PERCENT_RANK() OVER (
	PARTITION BY expr, ...
	ORDER BY expr [ASC | DESC], ...
)
```

## SQL 예제

이 예제는 PERCENT_RANK() 윈도 함수를 사용하여 학생의 이름, 점수, 등급을 조회하고 각 등급 내의 백분위 순위(percent_rank)를 구합니다.

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
