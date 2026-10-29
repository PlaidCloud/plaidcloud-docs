---
title: ARRAY_AGG (Lakehouse v1)
description: ARRAY_AGG – die Funktion ARRAY_AGG (auch unter dem Alias LIST bekannt) wandelt alle Werte um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-array-agg.md
---

Die Funktion ARRAY_AGG (auch unter dem Alias LIST bekannt) wandelt alle Werte einer bestimmten Spalte in einem Abfrageergebnis, einschließlich NULL, in ein Array um.

## Analyze-Syntax

```python
func.array_agg(<expr>)
```

## Analyze-Beispiele

```python
table.movie_title, func.array_agg(table.rating).alias('ratings')

| movie_title |  ratings   |
|-------------|------------|
| Inception   | [5, 4, 5]  |
```

## SQL-Syntax

```sql
ARRAY_AGG(<expr>)

LIST(<expr>)
```

## Argumente

| Argumente | Beschreibung   |
|-----------| -------------- |
| `<expr>`  | Beliebiger Ausdruck |

## Rückgabetyp

Gibt ein Array mit Elementen zurück, die denselben Typ wie die ursprünglichen Daten haben.

## SQL-Beispiele

Dieses Beispiel zeigt, wie die Funktion ARRAY_AGG verwendet werden kann, um Daten zu aggregieren und in einem praktischen Array-Format darzustellen:

```sql
-- Create a table and insert sample data
CREATE TABLE movie_ratings (
  id INT,
  movie_title VARCHAR,
  user_id INT,
  rating INT
);

INSERT INTO movie_ratings (id, movie_title, user_id, rating)
VALUES (1, 'Inception', 1, 5),
       (2, 'Inception', 2, 4),
       (3, 'Inception', 3, 5),
       (4, 'Interstellar', 1, 4),
       (5, 'Interstellar', 2, 3);

-- List all ratings for Inception in an array
SELECT movie_title, ARRAY_AGG(rating) AS ratings
FROM movie_ratings
WHERE movie_title = 'Inception'
GROUP BY movie_title;

| movie_title |  ratings   |
|-------------|------------|
| Inception   | [5, 4, 5]  |
```
