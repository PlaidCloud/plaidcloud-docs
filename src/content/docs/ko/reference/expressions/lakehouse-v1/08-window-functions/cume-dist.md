---
title: CUME_DIST (Lakehouse v1)
description: CUME_DIST — 값 집합에서 주어진 값의 누적 분포를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/cume-dist.md
---

값 집합에서 주어진 값의 누적 분포를 반환합니다. 지정한 값보다 작거나 같은 값을 가진 행의 비율을 전체 행 수로 나눈 값을 계산합니다. 참고로 결과 값은 0과 1 사이이며 0과 1을 포함합니다.

관련 항목: [PERCENT_RANK](../percent-rank/)

## Analyze 구문

```python
func.cume_dist().over(partition_by=[<columns>], order_by=[<columns>])
```

## Analyze 예제

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

## SQL 구문

```sql
CUME_DIST() OVER (
	PARTITION BY expr, ...
	ORDER BY expr [ASC | DESC], ...
)
```

## SQL 예제

이 예제는 CUME_DIST() 윈도우 함수를 사용하여 학생의 이름, 점수, 등급과 각 등급 내 누적 분포 값(cume_dist_val)을 가져옵니다.

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
