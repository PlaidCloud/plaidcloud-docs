---
title: NTILE (Lakehouse v1)
description: NTILE — divide o conjunto de resultados ordenado em um número especificado de baldes ou grupos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/ntile.md
---

Divide o conjunto de resultados ordenado em um número especificado de baldes ou grupos. Ela distribui uniformemente as linhas ordenadas entre esses baldes e atribui um número de balde a cada linha. A função NTILE é normalmente usada com a cláusula ORDER BY para ordenar os resultados. 

Observação: a função NTILE distribui uniformemente as linhas entre os baldes com base na ordem de classificação das linhas e garante que o número de linhas em cada balde seja o mais igual possível. Se o número de linhas não puder ser distribuído uniformemente entre os baldes, alguns baldes poderão ter uma linha a mais que os demais.

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

Este exemplo recupera os nomes, as notas e os conceitos dos alunos e os atribui a baldes com base em suas notas dentro de cada conceito, usando a função de janela NTILE().

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
