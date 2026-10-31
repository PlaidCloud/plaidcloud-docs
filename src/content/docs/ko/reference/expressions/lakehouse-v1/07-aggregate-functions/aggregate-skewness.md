---
title: SKEWNESS (Lakehouse v1)
description: SKEWNESS — 모든 입력 값의 왜도(분포의 비대칭 정도)를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-skewness.md
---

집계 함수입니다.

`SKEWNESS()` 함수는 모든 입력 값의 왜도를 반환합니다.

## Analyze 구문

```python
func.skewness(<expr>)
```

## Analyze 예제

```python
func.skewness(table.temperature).alias('temperature_skewness')

| temperature_skewness |
|----------------------|
|      0.68            |
```

## SQL 구문

```sql
SKEWNESS(<expr>)
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
CREATE TABLE temperature_data (
                                  id INT,
                                  city_id INT,
                                  temperature FLOAT
);

INSERT INTO temperature_data (id, city_id, temperature)
VALUES (1, 1, 60),
       (2, 1, 65),
       (3, 1, 62),
       (4, 2, 70),
       (5, 2, 75);
```

**쿼리 데모: 기온 데이터의 왜도 계산**

```sql
SELECT SKEWNESS(temperature) AS temperature_skewness
FROM temperature_data;
```

**결과**
```sql
| temperature_skewness |
|----------------------|
|      0.68            |
```
