---
title: MIN (Lakehouse v1)
description: MIN — 값 집합에서 최솟값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-min.md
---

집계 함수입니다.

MIN() 함수는 값 집합에서 최솟값을 반환합니다.

## Analyze 구문

```python
func.min(<column>)
```

## Analyze 예제

```python
table.station_id, func.min(table.price).alias('min_price')

| station_id | min_price |
|------------|-----------|
|     1      |   3.45    |
```

## SQL 구문

```sql
MIN(<expr>)
```

## 인수

| 인수 | 설명    |
|-----------|----------------|
| `<expr>`  | 모든 식 |

## 반환 형식

최솟값이며, 해당 값의 형식으로 반환됩니다.

## SQL 예제

---
title: MIN
---

집계 함수입니다.

MIN() 함수는 값 집합에서 최솟값을 반환합니다.

## SQL 구문

```sql
MIN(expression)
```

## 인수

| 인수   | 설명 |
| ----------- | ----------- |
| expression  | 모든 식 |

## 반환 형식

최솟값이며, 해당 값의 형식으로 반환됩니다.

## SQL 예제

**테이블을 만들고 샘플 데이터 삽입**
```sql
CREATE TABLE gas_prices (
  id INT,
  station_id INT,
  price FLOAT
);

INSERT INTO gas_prices (id, station_id, price)
VALUES (1, 1, 3.50),
       (2, 1, 3.45),
       (3, 1, 3.55),
       (4, 2, 3.40),
       (5, 2, 3.35);
```

**쿼리 데모: 1번 주유소의 최저 휘발유 가격 찾기**
```sql
SELECT station_id, MIN(price) AS min_price
FROM gas_prices
WHERE station_id = 1
GROUP BY station_id;
```

**결과**
```sql
| station_id | min_price |
|------------|-----------|
|     1      |   3.45    |
```
