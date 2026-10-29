---
title: NTILE (Lakehouse v1)
description: NTILE — divide el conjunto de resultados ordenado en un número especificado de cubos o grupos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/ntile.md
---

Divide el conjunto de resultados ordenado en un número especificado de cubos o grupos. Distribuye uniformemente las filas ordenadas en estos cubos y asigna un número de cubo a cada fila. La función NTILE se usa normalmente con la cláusula ORDER BY para ordenar los resultados. 

Tenga en cuenta que la función NTILE distribuye las filas uniformemente en cubos según el orden de las filas y procura que el número de filas de cada cubo sea lo más parecido posible. Si las filas no se pueden distribuir uniformemente en los cubos, algunos cubos pueden tener una fila más que los demás.

## Sintaxis de Analyze

```python
func.ntile(<n>).over(partition_by=[<columns>], order_by=[<columns>])
```

## Ejemplos de Analyze

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

## Sintaxis de SQL

```sql
NTILE(n) OVER (
	PARTITION BY expr, ...
	ORDER BY expr [ASC | DESC], ...
)
```

## Ejemplos de SQL

Este ejemplo obtiene los nombres, las puntuaciones y las calificaciones de los estudiantes, y los asigna a cubos según su puntuación dentro de cada calificación mediante la función de ventana NTILE().

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
