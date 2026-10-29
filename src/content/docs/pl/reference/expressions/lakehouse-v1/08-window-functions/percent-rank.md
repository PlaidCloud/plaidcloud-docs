---
title: PERCENT_RANK (Lakehouse v1)
description: PERCENT_RANK — zwraca względną pozycję danej wartości w zbiorze wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/percent-rank.md
---

Zwraca względną pozycję danej wartości w zbiorze wartości. Wynik mieści się w przedziale od 0 do 1 włącznie. Uwaga: pierwszy wiersz w każdym zbiorze ma wartość PERCENT_RANK równą 0.

Zobacz też: [CUME_DIST](../cume-dist)

## Składnia Analyze

```python
func.percent_rank().over(partition_by=[<columns>], order_by=[<columns>])
```

## Przykłady Analyze

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

## Składnia SQL

```sql
PERCENT_RANK() OVER (
	PARTITION BY expr, ...
	ORDER BY expr [ASC | DESC], ...
)
```

## Przykłady SQL

Ten przykład pobiera nazwiska uczniów, ich wyniki i oceny oraz rangi percentylowe (percent_rank) w obrębie każdej oceny, używając funkcji okna PERCENT_RANK().

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
