---
title: ARRAY_AGG (Lakehouse v1)
description: ARRAY_AGG — ARRAY_AGG 함수(별칭 LIST)는 모든 값을 배열로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-array-agg.md
---

ARRAY_AGG 함수(별칭 LIST)는 쿼리 결과에서 특정 열의 NULL을 포함한 모든 값을 배열로 변환합니다.

## Analyze 구문

```python
func.array_agg(<expr>)
```

## Analyze 예제

```python
table.movie_title, func.array_agg(table.rating).alias('ratings')

| movie_title |  ratings   |
|-------------|------------|
| Inception   | [5, 4, 5]  |
```

## SQL 구문

```sql
ARRAY_AGG(<expr>)

LIST(<expr>)
```

## 인수

| 인수 | 설명 |
|-----------| -------------- |
| `<expr>`  | 모든 식 |

## 반환 형식

원래 데이터와 같은 형식의 요소로 구성된 배열을 반환합니다.

## SQL 예제

이 예제는 ARRAY_AGG 함수로 데이터를 집계하여 편리한 배열 형태로 나타내는 방법을 보여 줍니다.

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
