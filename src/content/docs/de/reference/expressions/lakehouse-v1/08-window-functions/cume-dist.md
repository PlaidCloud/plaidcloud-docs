---
title: CUME_DIST (Lakehouse v1)
description: CUME_DIST – gibt die kumulative Verteilung eines bestimmten Werts in einer Wertemenge zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/cume-dist.md
---

Gibt die kumulative Verteilung eines bestimmten Werts in einer Wertemenge zurück. Sie berechnet den Anteil der Zeilen, deren Werte kleiner oder gleich dem angegebenen Wert sind, geteilt durch die Gesamtzahl der Zeilen. Bitte beachten Sie, dass der resultierende Wert zwischen 0 und 1 liegt (einschließlich).

Siehe auch: [PERCENT_RANK](../percent-rank/)

## Analyze-Syntax

```python
func.cume_dist().over(partition_by=[<columns>], order_by=[<columns>])
```

## Analyze-Beispiele

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

## SQL-Syntax

```sql
CUME_DIST() OVER (
	PARTITION BY expr, ...
	ORDER BY expr [ASC | DESC], ...
)
```

## SQL-Beispiele

Dieses Beispiel ruft mit der Fensterfunktion CUME_DIST() die Namen, Punktzahlen und Noten der Studierenden sowie die kumulativen Verteilungswerte (cume_dist_val) innerhalb jeder Note ab.

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
