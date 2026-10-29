---
title: GROUP_ARRAY_MOVING_SUM (Lakehouse v1)
description: GROUP_ARRAY_MOVING_SUM — GROUP_ARRAY_MOVING_SUM 함수는 입력 값의 이동 합계를 계산합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-group-array-moving-sum.md
---

GROUP_ARRAY_MOVING_SUM 함수는 입력 값의 이동 합계를 계산합니다. 이 함수는 윈도우 크기를 매개변수로 받을 수 있습니다. 지정하지 않으면 윈도우 크기는 입력 값의 개수와 같습니다.

## Analyze 구문

```python
func.group_array_moving_sum(<expr>)
```

## Analyze 예제

```python
table.user_id, func.group_array_moving_sum(table.request_num)

| user_id | request_num |
|---------|-------------|
|       1 | [10,23,43]  |
|       2 | [20,45,70]  |
|       3 | [15,36,62]  |
```

## SQL 구문

```sql
GROUP_ARRAY_MOVING_SUM(<expr>)

GROUP_ARRAY_MOVING_SUM(<window_size>)(<expr>)
```

## 인수

| 인수        | 설명              |
|------------------| ------------------------ |
| `<window_size>`  | 모든 숫자 식 |
| `<expr>`         | 모든 숫자 식 |

## 반환 형식

원래 데이터와 같은 형식의 요소로 구성된 배열을 반환합니다.

## SQL 예제

```sql
-- Create a table and insert sample data
CREATE TABLE hits (
  user_id INT,
  request_num INT
);

INSERT INTO hits (user_id, request_num)
VALUES (1, 10),
       (2, 15),
       (3, 20),
       (1, 13),
       (2, 21),
       (3, 25),
       (1, 30),
       (2, 41),
       (3, 45);

SELECT user_id, GROUP_ARRAY_MOVING_SUM(2)(request_num) AS request_num
FROM hits
GROUP BY user_id;

| user_id | request_num |
|---------|-------------|
|       1 | [10,23,43]  |
|       2 | [20,45,70]  |
|       3 | [15,36,62]  |
```
