---
title: COVAR_POP (Lakehouse v1)
description: COVAR_POP — COVAR_POP는 숫자 쌍 집합의 모공분산을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-covar-pop.md
---

COVAR_POP는 숫자 쌍 집합의 모공분산을 반환합니다.

## Analyze 구문

```python
func.covar_pop(<expr1>, <expr2>)
```

## Analyze 예제

```python
func.covar_pop(table.units_sold, table.revenue).alias('covar_pop_units_revenue')

| covar_pop_units_revenue |
|-------------------------|
|        20000.0          |
```

## SQL 구문

```sql
COVAR_POP(<expr1>, <expr2>)
```

## 인수

| 인수 |        설명       |
|-----------| ------------------------ |
| `<expr1>` | 모든 숫자 식 |
| `<expr2>` | 모든 숫자 식 |

## 반환 형식

float64

## SQL 예제

**테이블을 만들고 샘플 데이터 삽입**
```sql
CREATE TABLE product_sales (
  id INT,
  product_id INT,
  units_sold INT,
  revenue FLOAT
);

INSERT INTO product_sales (id, product_id, units_sold, revenue)
VALUES (1, 1, 10, 1000),
       (2, 2, 20, 2000),
       (3, 3, 30, 3000),
       (4, 4, 40, 4000),
       (5, 5, 50, 5000);
```

**쿼리 데모: 판매 수량과 매출 간의 모공분산 계산**

```sql
SELECT COVAR_POP(units_sold, revenue) AS covar_pop_units_revenue
FROM product_sales;
```

**결과**
```sql
| covar_pop_units_revenue |
|-------------------------|
|        20000.0          |
```
