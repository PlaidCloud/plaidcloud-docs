---
title: APPROX_COUNT_DISTINCT (Lakehouse v1)
description: APPROX_COUNT_DISTINCT — HyperLogLog 알고리즘으로 데이터 집합의 고유 값 개수를 추정합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-approx-count-distinct.md
---

[HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog) 알고리즘으로 데이터 집합의 고유 값 개수를 추정합니다.

HyperLogLog 알고리즘은 적은 메모리와 시간으로 고유 요소 수의 근삿값을 제공합니다. 추정 결과를 허용할 수 있는 대규모 데이터 집합을 다룰 때 이 함수를 사용해 보십시오. 약간의 정확도를 희생하는 대신, 고유 개수를 빠르고 효율적으로 반환하는 방법입니다.

정확한 결과가 필요하면 [COUNT_DISTINCT](../aggregate-count-distinct)를 사용하십시오. 자세한 설명은 [예제](#sql-예제)를 참조하십시오.

## Analyze 구문

```python
func.approx_count_distinct(<expr>)
```

## Analyze 예제

```python
func.approx_count_distinct(table.user_id).alias('approx_distinct_user_count')

| approx_distinct_user_count |
|----------------------------|
|             4              |
```

## SQL 구문

```sql
APPROX_COUNT_DISTINCT(<expr>)
```

## 반환 형식

정수입니다.

## SQL 예제

**테이블을 만들고 샘플 데이터 삽입**
```sql
CREATE TABLE user_events (
  id INT,
  user_id INT,
  event_name VARCHAR
);

INSERT INTO user_events (id, user_id, event_name)
VALUES (1, 1, 'Login'),
       (2, 2, 'Login'),
       (3, 3, 'Login'),
       (4, 1, 'Logout'),
       (5, 2, 'Logout'),
       (6, 4, 'Login'),
       (7, 1, 'Login');
```

**쿼리 데모: 고유 사용자 ID 개수 추정**
```sql
SELECT APPROX_COUNT_DISTINCT(user_id) AS approx_distinct_user_count
FROM user_events;
```

**결과**
```sql
| approx_distinct_user_count |
|----------------------------|
|             4              |
```
