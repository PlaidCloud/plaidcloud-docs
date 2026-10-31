---
title: ARRAY_AGG (Lakehouse v1)
description: ARRAY_AGG — a função ARRAY_AGG (também conhecida pelo alias LIST) transforma todos os valores.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-array-agg.md
---

A função ARRAY_AGG (também conhecida pelo alias LIST) transforma todos os valores, inclusive NULL, de uma coluna específica no resultado de uma consulta em um array.

## Sintaxe do Analyze

```python
func.array_agg(<expr>)
```

## Exemplos do Analyze

```python
table.movie_title, func.array_agg(table.rating).alias('ratings')

| movie_title |  ratings   |
|-------------|------------|
| Inception   | [5, 4, 5]  |
```

## Sintaxe SQL

```sql
ARRAY_AGG(<expr>)

LIST(<expr>)
```

## Argumentos

| Argumentos | Descrição        |
|-----------| ---------------- |
| `<expr>`  | Qualquer expressão |

## Tipo de retorno

Retorna um array com elementos do mesmo tipo que os dados originais.

## Exemplos de SQL

Este exemplo demonstra como a função ARRAY_AGG pode ser usada para agregar e apresentar dados em um formato de array conveniente:

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
