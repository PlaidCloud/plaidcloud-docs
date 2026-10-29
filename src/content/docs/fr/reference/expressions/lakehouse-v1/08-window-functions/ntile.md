---
title: NTILE (Lakehouse v1)
description: NTILE — répartit le jeu de résultats trié en un nombre donné de tranches ou de groupes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/ntile.md
---

Répartit le jeu de résultats trié en un nombre donné de tranches (buckets) ou de groupes. La fonction distribue uniformément les lignes triées dans ces tranches et attribue à chaque ligne un numéro de tranche. NTILE s'utilise généralement avec la clause ORDER BY pour trier les résultats.

À noter : la fonction NTILE répartit les lignes dans les tranches selon leur ordre de tri et veille à ce que le nombre de lignes de chaque tranche soit aussi proche que possible. Si les lignes ne peuvent pas être réparties de façon égale, certaines tranches peuvent compter une ligne de plus que les autres.

## Syntaxe Analyze

```python
func.ntile(<n>).over(partition_by=[<columns>], order_by=[<columns>])
```

## Exemples Analyze

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

## Syntaxe SQL

```sql
NTILE(n) OVER (
	PARTITION BY expr, ...
	ORDER BY expr [ASC | DESC], ...
)
```

## Exemples SQL

Cet exemple récupère les noms, les notes et les niveaux des élèves, puis les affecte à des tranches selon leur note au sein de chaque niveau, à l'aide de la fonction de fenêtrage NTILE().

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
