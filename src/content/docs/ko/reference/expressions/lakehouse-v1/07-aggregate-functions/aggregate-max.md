---
title: MAX (Lakehouse v1)
description: MAX — 값 집합에서 최댓값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-max.md
---

집계 함수입니다.

MAX() 함수는 값 집합에서 최댓값을 반환합니다.

## Analyze 구문

```python
func.max(<column>)
```

## Analyze 예제

```python
table.city, func.max(table.temperature).alias('max_temperature')

|    city    | max_temperature |
|------------|-----------------|
| New York   |       32        |
```

## SQL 구문

```sql
MAX(<expr>)
```

## 인수

| 인수 | 설명 |
|-----------| ----------- |
| `<expr>`  | 모든 식 |

## 반환 형식

최댓값이며, 해당 값의 형식으로 반환됩니다.

## SQL 예제

**테이블을 만들고 샘플 데이터 삽입**
```sql
CREATE TABLE temperatures (
  id INT,
  city VARCHAR,
  temperature FLOAT
);

INSERT INTO temperatures (id, city, temperature)
VALUES (1, 'New York', 30),
       (2, 'New York', 28),
       (3, 'New York', 32),
       (4, 'Los Angeles', 25),
       (5, 'Los Angeles', 27);
```

**쿼리 데모: 뉴욕시의 최고 기온 찾기**

```sql
SELECT city, MAX(temperature) AS max_temperature
FROM temperatures
WHERE city = 'New York'
GROUP BY city;
```

**결과**
```sql
|    city    | max_temperature |
|------------|-----------------|
| New York   |       32        |
```
