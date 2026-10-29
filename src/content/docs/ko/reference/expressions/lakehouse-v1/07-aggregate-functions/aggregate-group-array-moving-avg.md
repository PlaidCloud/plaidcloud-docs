---
title: GROUP_ARRAY_MOVING_AVG (Lakehouse v1)
description: GROUP_ARRAY_MOVING_AVG — GROUP_ARRAY_MOVING_AVG 함수는 입력 값의 이동 평균을 계산합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-group-array-moving-avg.md
---

GROUP_ARRAY_MOVING_AVG 함수는 입력 값의 이동 평균을 계산합니다. 이 함수는 윈도우 크기를 매개변수로 받을 수 있습니다. 지정하지 않으면 윈도우 크기는 입력 값의 개수와 같습니다.

## Analyze 구문

```python
func.group_array_moving_avg(<expr1>)
```

## Analyze 예제

```python
table.user_id, func.group_array_moving_avg(table.request_num).alias('avg_request_num')

| user_id | avg_request_num  |
|---------|------------------|
|       1 | [5.0,11.5,21.5]  |
|       3 | [10.0,22.5,35.0] |
|       2 | [7.5,18.0,31.0]  |
```

## SQL 구문

```sql
GROUP_ARRAY_MOVING_AVG(<expr>)

GROUP_ARRAY_MOVING_AVG(<window_size>)(<expr>)
```

## 인수

| 인수        | 설명              |
|------------------| ------------------------ |
| `<window_size>`  | 모든 숫자 식 |
| `<expr>`         | 모든 숫자 식 |

## 반환 형식

원본 데이터 형식에 따라 double 또는 decimal 요소로 구성된 배열을 반환합니다.

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

SELECT user_id, GROUP_ARRAY_MOVING_AVG(2)(request_num) AS avg_request_num
FROM hits
GROUP BY user_id;

| user_id | avg_request_num  |
|---------|------------------|
|       1 | [5.0,11.5,21.5]  |
|       3 | [10.0,22.5,35.0] |
|       2 | [7.5,18.0,31.0]  |
```
