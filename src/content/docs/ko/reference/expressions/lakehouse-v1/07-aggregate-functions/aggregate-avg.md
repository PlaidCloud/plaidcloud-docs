---
title: AVG (Lakehouse v1)
description: AVG — NULL 값을 무시하고 식의 평균값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-avg.md
---

집계 함수입니다.

AVG() 함수는 식의 평균값을 반환합니다.

**참고:** NULL 값은 계산에 포함되지 않습니다.


## Analyze 구문

```python
func.avg(<column>)
```

## Analyze 예제

```python
func.avg(table.price).alias('avg_price')

| avg_price |
| --------- |
| 20.4      |
```

## SQL 구문

```sql
AVG(<expr>)
```

## 인수

| 인수 | 설명 |
|-----------|--------------------------|
| `<expr>`  | 모든 숫자 식 |

## 반환 형식

double

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

**쿼리: AVG() 함수 사용**

이제 AVG() 함수를 사용하여 "sales" 테이블에 있는 모든 제품의 평균 가격을 구합니다.
```sql
SELECT AVG(price) AS avg_price
FROM sales;
```

결과는 다음과 같습니다.
```sql
| avg_price |
| --------- |
| 20.4      |
```
