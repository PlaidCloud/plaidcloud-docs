---
title: ARRAY_AGG (Lakehouse v1)
description: ARRAY_AGG — ARRAY_AGG 関数（エイリアスは LIST）は、すべての値を配列に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-array-agg.md
---

ARRAY_AGG 関数（エイリアスは LIST）は、クエリ結果内の特定の列のすべての値（NULL を含む）を配列に変換します。

## Analyzeの構文

```python
func.array_agg(<expr>)
```

## Analyzeの例

```python
table.movie_title, func.array_agg(table.rating).alias('ratings')

| movie_title |  ratings   |
|-------------|------------|
| Inception   | [5, 4, 5]  |
```

## SQLの構文

```sql
ARRAY_AGG(<expr>)

LIST(<expr>)
```

## 引数

| 引数 | 説明 |
|-----------| -------------- |
| `<expr>`  | 任意の式 |

## 戻り値の型

元のデータと同じ型の要素を持つ配列を返します。

## SQLの例

この例は、ARRAY_AGG 関数を使用して、データを扱いやすい配列形式に集計して表示する方法を示しています。

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
