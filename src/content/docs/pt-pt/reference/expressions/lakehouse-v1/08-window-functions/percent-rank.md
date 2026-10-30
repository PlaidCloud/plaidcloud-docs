---
title: PERCENT_RANK (Lakehouse v1)
description: PERCENT_RANK — devolve a classificação relativa de um valor dado dentro de um conjunto de valores.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/percent-rank.md
---

Devolve a classificação relativa de um valor dado dentro de um conjunto de valores. O valor resultante situa-se entre 0 e 1, inclusive. Tenha em atenção que a primeira linha de qualquer conjunto tem um PERCENT_RANK de 0.

Ver também: [CUME_DIST](../cume-dist)

## Sintaxe do Analyze

```python
func.percent_rank().over(partition_by=[<columns>], order_by=[<columns>])
```

## Exemplos do Analyze

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

## Sintaxe SQL

```sql
PERCENT_RANK() OVER (
	PARTITION BY expr, ...
	ORDER BY expr [ASC | DESC], ...
)
```

## Exemplos de SQL

Este exemplo obtém os nomes, as pontuações e as classificações dos alunos, bem como as classificações percentuais (percent_rank) dentro de cada classificação, utilizando a função de janela PERCENT_RANK().

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
