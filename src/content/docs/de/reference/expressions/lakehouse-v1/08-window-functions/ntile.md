---
title: NTILE (Lakehouse v1)
description: NTILE — teilt die sortierte Ergebnismenge in eine festgelegte Anzahl von Buckets bzw. Gruppen auf.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/ntile.md
---

Teilt die sortierte Ergebnismenge in eine festgelegte Anzahl von Buckets bzw. Gruppen auf. Die Funktion verteilt die sortierten Zeilen gleichmäßig auf diese Buckets und weist jeder Zeile eine Bucket-Nummer zu. Die Funktion NTILE wird typischerweise zusammen mit der ORDER-BY-Klausel verwendet, um die Ergebnisse zu sortieren.

Bitte beachten: Die Funktion NTILE verteilt die Zeilen anhand ihrer Sortierreihenfolge gleichmäßig auf Buckets und stellt sicher, dass die Anzahl der Zeilen in jedem Bucket so gleich wie möglich ist. Lassen sich die Zeilen nicht gleichmäßig auf die Buckets verteilen, enthalten einige Buckets eine Zeile mehr als die übrigen.

## Analyze-Syntax

```python
func.ntile(<n>).over(partition_by=[<columns>], order_by=[<columns>])
```

## Analyze-Beispiele

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

## SQL-Syntax

```sql
NTILE(n) OVER (
	PARTITION BY expr, ...
	ORDER BY expr [ASC | DESC], ...
)
```

## SQL-Beispiele

Dieses Beispiel ruft die Namen, Punktzahlen und Noten von Schülern ab und weist sie mit der Fensterfunktion NTILE() anhand ihrer Punktzahlen innerhalb der jeweiligen Note Buckets zu.

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
