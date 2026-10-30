---
title: CUME_DIST (Lakehouse v1)
description: CUME_DIST — devolve a distribuição cumulativa de um determinado valor num conjunto de valores.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/cume-dist.md
---

Devolve a distribuição cumulativa de um determinado valor num conjunto de valores. Calcula a proporção de linhas com valores inferiores ou iguais ao valor especificado, dividida pelo número total de linhas. Tenha em atenção que o valor resultante se situa entre 0 e 1, inclusive.

Consulte também: [PERCENT_RANK](../percent-rank/)

## Sintaxe do Analyze

```python
func.cume_dist().over(partition_by=[<columns>], order_by=[<columns>])
```

## Exemplos do Analyze

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

## Sintaxe SQL

```sql
CUME_DIST() OVER (
	PARTITION BY expr, ...
	ORDER BY expr [ASC | DESC], ...
)
```

## Exemplos de SQL

Este exemplo obtém os nomes, as pontuações e as classificações dos alunos, bem como os valores de distribuição cumulativa (cume_dist_val) dentro de cada classificação, através da função de janela CUME_DIST().

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
