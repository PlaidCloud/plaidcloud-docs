---
title: RETENTION (Lakehouse v1)
description: RETENTION — 집계 함수입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-retention.md
---

집계 함수입니다.

RETENTION() 함수는 이벤트에 대해 특정 조건이 충족되었는지 나타내는 UInt8 형식의 조건 1개에서 32개를 인수로 받습니다.

모든 조건을 인수로 지정할 수 있습니다(WHERE에서와 같습니다).

첫 번째를 제외한 조건은 쌍으로 적용됩니다. 두 번째 조건의 결과는 첫 번째와 두 번째가 모두 참이면 참이고, 세 번째 조건의 결과는 첫 번째와 세 번째가 모두 참이면 참이며, 이후도 같은 방식입니다.

## Analyze 구문

```python
func.retention(<cond1> , <cond2> , ..., <cond32>)
```

## Analyze 예제

```python
table.user_id, func.retention(table.event_type=='signup', table.event_type='login', table.event_type='purchase').alias('sales_amounts')

| user_id | retention |
|---------|-----------|
|   1     | [1, 1, 0] |
|   2     | [1, 0, 1] |
|   3     | [1, 1, 0] |
```

## SQL 구문

```sql
RETENTION( <cond1> , <cond2> , ..., <cond32> );
```

## 인수

| 인수 | 설명                                 |
|-----------|---------------------------------------------|
| `<cond>`  | 부울 결과를 반환하는 식 |

## 반환 형식

1 또는 0으로 이루어진 배열입니다.

## SQL 예제

**테이블을 만들고 샘플 데이터 삽입**
```sql
CREATE TABLE user_events (
  id INT,
  user_id INT,
  event_date DATE,
  event_type VARCHAR
);

INSERT INTO user_events (id, user_id, event_date, event_type)
VALUES (1, 1, '2022-01-01', 'signup'),
       (2, 1, '2022-01-02', 'login'),
       (3, 2, '2022-01-01', 'signup'),
       (4, 2, '2022-01-03', 'purchase'),
       (5, 3, '2022-01-01', 'signup'),
       (6, 3, '2022-01-02', 'login');
```

**쿼리 데모: 가입, 로그인, 구매 이벤트를 기준으로 사용자 리텐션 계산**
```sql
SELECT
  user_id,
  RETENTION(event_type = 'signup', event_type = 'login', event_type = 'purchase') AS retention
FROM user_events
GROUP BY user_id;
```

**결과**
```sql
| user_id | retention |
|---------|-----------|
|   1     | [1, 1, 0] |
|   2     | [1, 0, 1] |
|   3     | [1, 1, 0] |
```
