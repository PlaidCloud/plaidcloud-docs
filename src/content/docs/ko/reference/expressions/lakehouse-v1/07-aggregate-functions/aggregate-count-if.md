---
title: COUNT_IF (Lakehouse v1)
description: COUNT_IF — 접미사 _IF를 모든 집계 함수 이름 뒤에 붙일 수 있습니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-count-if.md
---

접미사 `_IF`를 모든 집계 함수 이름 뒤에 붙일 수 있습니다. 이 경우 집계 함수는 조건이라는 추가 인수를 받습니다.

## Analyze 구문

```python
func.count_if(<column>, <cond>)
```

## Analyze 예제

```python
func.count_if(table.status, table.status=='Completed').alias('completed_orders')

| completed_orders |
|------------------|
|        3         |
```

## SQL 예제
```sql
COUNT_IF(<column>, <cond>)
```

## SQL 예제

**테이블을 만들고 샘플 데이터 삽입**
```sql
CREATE TABLE orders (
  id INT,
  customer_id INT,
  status VARCHAR,
  total FLOAT
);

INSERT INTO orders (id, customer_id, status, total)
VALUES (1, 1, 'completed', 100),
       (2, 2, 'completed', 200),
       (3, 1, 'pending', 150),
       (4, 3, 'completed', 250),
       (5, 2, 'pending', 300);
```

**쿼리 데모: 완료된 주문 수 세기**
```sql
SELECT COUNT_IF(status, status = 'completed') AS completed_orders
FROM orders;
```

**결과**
```sql
| completed_orders |
|------------------|
|        3         |
```
