---
title: MAX_IF (Lakehouse v1)
description: MAX_IF — 접미사 _IF를 모든 집계 함수 이름 뒤에 붙일 수 있습니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-max-if.md
---

접미사 `_IF`를 모든 집계 함수 이름 뒤에 붙일 수 있습니다. 이 경우 집계 함수는 조건이라는 추가 인수를 받습니다.

## Analyze 구문

```python
func.max_if(<column>, <cond>)
```

## Analyze 예제

```python
func.max_if(table.revenue, table.salesperson_id==1).alias('max_revenue_salesperson_1')

| max_revenue_salesperson_1 |
|---------------------------|
|           3000            |
```

## SQL 예제

```sql
MAX_IF(<column>, <cond>)
```

## SQL 예제

**테이블을 만들고 샘플 데이터 삽입**
```sql
CREATE TABLE sales (
  id INT,
  salesperson_id INT,
  product_id INT,
  revenue FLOAT
);

INSERT INTO sales (id, salesperson_id, product_id, revenue)
VALUES (1, 1, 1, 1000),
       (2, 1, 2, 2000),
       (3, 1, 3, 3000),
       (4, 2, 1, 1500),
       (5, 2, 2, 2500);
```

**쿼리 데모: ID가 1인 영업 담당자의 최대 매출 찾기**

```sql
SELECT MAX_IF(revenue, salesperson_id = 1) AS max_revenue_salesperson_1
FROM sales;
```

**결과**
```sql
| max_revenue_salesperson_1 |
|---------------------------|
|           3000            |
```
