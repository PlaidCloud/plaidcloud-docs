---
title: SCORE (Lakehouse v1)
description: SCORE — 쿼리 문자열의 관련도를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-search-functions/score.md
---

쿼리 문자열의 관련도를 반환합니다. 점수가 높을수록 데이터의 관련도가 높습니다. 참고: SCORE 함수는 [QUERY](../query) 또는 [MATCH](../match) 함수와 함께만 사용할 수 있습니다.

:::info
PlaidCloud Lakehouse의 SCORE 함수는 Elasticsearch의 [SCORE](https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-functions-search.html#sql-functions-search-score)에서 착안했습니다.
:::

## SQL Syntax

```sql
SCORE()
```

## SQL Examples

```sql
CREATE TABLE test(title STRING, body STRING);

CREATE INVERTED INDEX idx ON test(title, body);

INSERT INTO test VALUES
('The Importance of Reading', 'Reading is a crucial skill that opens up a world of knowledge and imagination.'),
('The Benefits of Exercise', 'Exercise is essential for maintaining a healthy lifestyle.'),
('The Power of Perseverance', 'Perseverance is the key to overcoming obstacles and achieving success.'),
('The Art of Communication', 'Effective communication is crucial in everyday life.'),
('The Impact of Technology on Society', 'Technology has revolutionized our society in countless ways.');

-- Retrieve documents where the 'title' column contains the keyword 'art' with a boost of 5 and the 'body' column contains the keyword 'reading' with a boost of 1.2, along with their relevance scores
SELECT *, score() FROM test WHERE QUERY('title:art^5 body:reading^1.2');

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│           title           │                                      body                                      │  score()  │
├───────────────────────────┼────────────────────────────────────────────────────────────────────────────────┼───────────┤
│ The Importance of Reading │ Reading is a crucial skill that opens up a world of knowledge and imagination. │ 1.3860708 │
│ The Art of Communication  │ Effective communication is crucial in everyday life.                           │ 7.1992116 │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

-- Retrieve documents where the 'title' column contains the keyword 'reading' with a boost of 5 and the 'body' column contains the keyword 'everyday' with a boost of 1.2, along with their relevance scores
SELECT *, score() FROM test WHERE MATCH('title^5, body^1.2', 'reading everyday');

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│           title           │                                      body                                      │  score()  │
├───────────────────────────┼────────────────────────────────────────────────────────────────────────────────┼───────────┤
│ The Importance of Reading │ Reading is a crucial skill that opens up a world of knowledge and imagination. │  8.585282 │
│ The Art of Communication  │ Effective communication is crucial in everyday life.                           │ 1.8575745 │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
