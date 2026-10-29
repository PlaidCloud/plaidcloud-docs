---
title: ARRAY_AGG (Lakehouse v1)
description: "ARRAY_AGG: la función ARRAY_AGG (también conocida por su alias LIST) transforma todos los valores."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-array-agg.md
---

La función ARRAY_AGG (también conocida por su alias LIST) transforma todos los valores, incluido NULL, de una columna específica del resultado de una consulta en una matriz.

## Sintaxis de Analyze

```python
func.array_agg(<expr>)
```

## Ejemplos de Analyze

```python
table.movie_title, func.array_agg(table.rating).alias('ratings')

| movie_title |  ratings   |
|-------------|------------|
| Inception   | [5, 4, 5]  |
```

## Sintaxis de SQL

```sql
ARRAY_AGG(<expr>)

LIST(<expr>)
```

## Argumentos

| Argumentos | Descripción    |
|-----------| -------------- |
| `<expr>`  | Cualquier expresión |

## Tipo de valor devuelto

Devuelve una matriz con elementos del mismo tipo que los datos originales.

## Ejemplos de SQL

Este ejemplo muestra cómo se puede usar la función ARRAY_AGG para agregar y presentar los datos en un formato de matriz práctico:

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
