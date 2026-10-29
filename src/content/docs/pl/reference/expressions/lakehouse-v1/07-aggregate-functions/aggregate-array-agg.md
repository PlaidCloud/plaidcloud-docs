---
title: ARRAY_AGG (Lakehouse v1)
description: ARRAY_AGG — funkcja ARRAY_AGG (znana także pod aliasem LIST) przekształca wszystkie wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-array-agg.md
---

Funkcja ARRAY_AGG (znana także pod aliasem LIST) przekształca wszystkie wartości wybranej kolumny w wyniku zapytania, w tym NULL, w tablicę.

## Składnia Analyze

```python
func.array_agg(<expr>)
```

## Przykłady Analyze

```python
table.movie_title, func.array_agg(table.rating).alias('ratings')

| movie_title |  ratings   |
|-------------|------------|
| Inception   | [5, 4, 5]  |
```

## Składnia SQL

```sql
ARRAY_AGG(<expr>)

LIST(<expr>)
```

## Argumenty

| Argumenty | Opis           |
|-----------| -------------- |
| `<expr>`  | Dowolne wyrażenie |

## Typ zwracany

Zwraca tablicę z elementami tego samego typu co dane oryginalne.

## Przykłady SQL

Ten przykład pokazuje, jak funkcji ARRAY_AGG można użyć do agregowania i prezentowania danych w wygodnym formacie tablicy:

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
