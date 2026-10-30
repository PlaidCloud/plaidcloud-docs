---
title: NTILE (Lakehouse v1)
description: NTILE — dzieli posortowany zbiór wyników na określoną liczbę przedziałów lub grup.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/ntile.md
---

Dzieli posortowany zbiór wyników na określoną liczbę przedziałów lub grup. Równomiernie rozdziela posortowane wiersze między te przedziały i przypisuje każdemu wierszowi numer przedziału. Funkcję NTILE zazwyczaj stosuje się z klauzulą ORDER BY, aby posortować wyniki. 

Uwaga: funkcja NTILE rozdziela wiersze na przedziały zgodnie z kolejnością sortowania i dba o to, aby liczba wierszy w poszczególnych przedziałach była jak najbardziej zbliżona. Jeśli wierszy nie da się rozdzielić równo, niektóre przedziały mogą mieć o jeden wiersz więcej niż pozostałe.

## Składnia Analyze

```python
func.ntile(<n>).over(partition_by=[<columns>], order_by=[<columns>])
```

## Przykłady Analyze

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

## Składnia SQL

```sql
NTILE(n) OVER (
	PARTITION BY expr, ...
	ORDER BY expr [ASC | DESC], ...
)
```

## Przykłady SQL

Ten przykład pobiera nazwiska uczniów, ich wyniki i oceny oraz przypisuje ich do przedziałów na podstawie wyników w obrębie każdej oceny, używając funkcji okna NTILE().

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
