---
title: ARRAY_AGG (Lakehouse v1)
description: "ARRAY_AGG : la fonction ARRAY_AGG (également connue sous son alias LIST) transforme toutes les valeurs."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-array-agg.md
---

La fonction ARRAY_AGG (également connue sous son alias LIST) transforme toutes les valeurs d'une colonne donnée d'un résultat de requête, y compris NULL, en un tableau.

## Syntaxe Analyze

```python
func.array_agg(<expr>)
```

## Exemples Analyze

```python
table.movie_title, func.array_agg(table.rating).alias('ratings')

| movie_title |  ratings   |
|-------------|------------|
| Inception   | [5, 4, 5]  |
```

## Syntaxe SQL

```sql
ARRAY_AGG(<expr>)

LIST(<expr>)
```

## Arguments

| Arguments | Description    |
|-----------| -------------- |
| `<expr>`  | Toute expression |

## Type de retour

Renvoie un tableau dont les éléments sont du même type que les données d'origine.

## Exemples SQL

Cet exemple montre comment la fonction ARRAY_AGG permet d'agréger et de présenter des données sous la forme pratique d'un tableau :

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
