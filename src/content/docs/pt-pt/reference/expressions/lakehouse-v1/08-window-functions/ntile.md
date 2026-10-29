---
title: NTILE (Lakehouse v1)
description: NTILE — divide o conjunto de resultados ordenado num número especificado de baldes ou grupos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/ntile.md
---

Divide o conjunto de resultados ordenado num número especificado de baldes ou grupos. Distribui uniformemente as linhas ordenadas por esses baldes e atribui um número de balde a cada linha. A função NTILE é normalmente utilizada com a cláusula ORDER BY para ordenar os resultados. 

Tenha em atenção que a função NTILE distribui uniformemente as linhas pelos baldes com base na ordem de ordenação das linhas e garante que o número de linhas em cada balde é o mais igual possível. Se não for possível distribuir uniformemente as linhas pelos baldes, alguns baldes podem ter mais uma linha do que os outros.

## Sintaxe do Analyze

```python
func.ntile(<n>).over(partition_by=[<columns>], order_by=[<columns>])
```

## Exemplos do Analyze

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

## Sintaxe SQL

```sql
NTILE(n) OVER (
	PARTITION BY expr, ...
	ORDER BY expr [ASC | DESC], ...
)
```

## Exemplos de SQL

Este exemplo obtém os nomes, as pontuações e as classificações dos alunos e atribui-os a baldes com base nas respetivas pontuações dentro de cada classificação, utilizando a função de janela NTILE().

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
