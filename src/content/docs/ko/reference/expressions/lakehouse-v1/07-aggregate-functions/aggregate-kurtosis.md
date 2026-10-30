---
title: KURTOSIS (Lakehouse v1)
description: KURTOSIS — 모든 입력 값의 초과 첨도(정규분포 대비 뾰족한 정도)를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-kurtosis.md
---

집계 함수입니다.

`KURTOSIS()` 함수는 모든 입력 값의 초과 첨도를 반환합니다.

## Analyze 구문

```python
func.kurtosis(<expr>)
```

## Analyze 예제

```python
func.kurtosis(table.price).alias('excess_kurtosis')

|     excess_kurtosis     |
|-------------------------|
| 0.06818181325581445     |
```

## SQL 구문

```sql
KURTOSIS(<expr>)
```

## 인수

| 인수 | 설명                     |
|-----------| -----------                     |
| `<expr>`  | 모든 숫자 식        |

## 반환 형식

Nullable Float64입니다.

## SQL 예제

**테이블을 만들고 샘플 데이터 삽입**
```sql
CREATE TABLE stock_prices (
  id INT,
  stock_symbol VARCHAR,
  price FLOAT
);

INSERT INTO stock_prices (id, stock_symbol, price)
VALUES (1, 'AAPL', 150),
       (2, 'AAPL', 152),
       (3, 'AAPL', 148),
       (4, 'AAPL', 160),
       (5, 'AAPL', 155);
```

**쿼리 데모: Apple 주가의 초과 첨도 계산**

```sql
SELECT KURTOSIS(price) AS excess_kurtosis
FROM stock_prices
WHERE stock_symbol = 'AAPL';
```

**결과**

```sql
|     excess_kurtosis     |
|-------------------------|
| 0.06818181325581445     |
```
