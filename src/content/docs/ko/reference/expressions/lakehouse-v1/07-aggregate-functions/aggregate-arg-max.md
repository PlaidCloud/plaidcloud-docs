---
title: ARG_MAX (Lakehouse v1)
description: ARG_MAX — val 값이 최대일 때의 arg 값을 계산합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-arg-max.md
---

`val` 값이 최대일 때의 `arg` 값을 계산합니다. `val`의 최댓값에 해당하는 `arg` 값이 여러 개이면 처음 만나는 값을 반환합니다.

## Analyze 구문

```python
func.arg_max(<expr>)
```

## Analyze 예제

```python
func.arg_max(table.product, table.price).alias('max_price_product')

| max_price_product |
| ----------------- |
| Product C         |
```

## SQL 구문

```sql
ARG_MAX(<arg>, <val>)
```

## 인수

| 인수 | 설명 |
|-----------|---------------------------------------------------------------------------------------------------|
| `<arg>`   | PlaidCloud Lakehouse가 지원하는 모든 데이터 형식의 인수 |
| `<val>`   | PlaidCloud Lakehouse가 지원하는 모든 데이터 형식의 값 |

## 반환 형식

`val` 값이 최대일 때의 `arg` 값입니다.

 `arg` 형식과 일치합니다.

## SQL 예제

**테이블을 만들고 샘플 데이터 삽입**

"sales"라는 테이블을 만들고 샘플 데이터를 삽입합니다.
```sql
CREATE TABLE sales (
  id INTEGER,
  product VARCHAR(50),
  price FLOAT
);

INSERT INTO sales (id, product, price)
VALUES (1, 'Product A', 10.5),
       (2, 'Product B', 20.75),
       (3, 'Product C', 30.0),
       (4, 'Product D', 15.25),
       (5, 'Product E', 25.5);
```

**쿼리: ARG_MAX() 함수 사용**

이제 ARG_MAX() 함수를 사용하여 가격이 가장 높은 제품을 찾습니다.
```sql
SELECT ARG_MAX(product, price) AS max_price_product
FROM sales;
```

결과는 다음과 같습니다.
```sql
| max_price_product |
| ----------------- |
| Product C         |
```
