---
title: SUM_IF (Lakehouse v1)
description: SUM_IF — 접미사 -If를 모든 집계 함수 이름 뒤에 붙일 수 있습니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-sum-if.md
---

접미사 -If를 모든 집계 함수 이름 뒤에 붙일 수 있습니다. 이 경우 집계 함수는 조건이라는 추가 인수를 받습니다.

## Analyze 구문

```python
func.sum_if(<column>, <cond>)
```

## Analyze 예제

```python
func.sum_if(table.amount, table.status=='Completed').alias('total_amount_completed')

| total_amount_completed |
|------------------------|
|         270.0          |
```

## SQL 구문

```sql
SUM_IF(<column>, <cond>)
```

## SQL 예제

**테이블을 만들고 샘플 데이터 삽입**
```sql
CREATE TABLE order_data (
  id INT,
  customer_id INT,
  amount FLOAT,
  status VARCHAR
);

INSERT INTO order_data (id, customer_id, amount, status)
VALUES (1, 1, 100, 'Completed'),
       (2, 2, 50, 'Completed'),
       (3, 3, 80, 'Cancelled'),
       (4, 4, 120, 'Completed'),
       (5, 5, 75, 'Cancelled');
```

**쿼리 데모: 완료된 주문의 총액 계산**
```sql
SELECT SUM_IF(amount, status = 'Completed') AS total_amount_completed
FROM order_data;
```

**결과**
```sql
| total_amount_completed |
|------------------------|
|         270.0          |
```
