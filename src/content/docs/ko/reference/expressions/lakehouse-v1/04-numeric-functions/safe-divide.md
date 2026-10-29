---
title: SAFE_DIVIDE (Lakehouse v1)
description: SAFE_DIVIDE — 두 수를 나누고, 분모가 0일 때 실패하는 대신 사용자가 선택한 값을 반환하는 PlaidCloud 함수입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/safe-divide.md
---

모든 레이크하우스 엔진에서 사용할 수 있는 PlaidCloud 함수입니다. 첫 번째 수를 두 번째 수로 나눕니다. 분모가 0이거나 어느 한쪽이 NULL이면 결과는 세 번째 값입니다. NULL을 얻으려면 `None`을 전달합니다. Lakehouse v1에서는 세 인수가 모두 필수입니다. 정수 열도 잘림 없이 나누어지도록 양쪽을 먼저 `DECIMAL(38, 10)`으로 캐스팅합니다.

## Analyze 구문

```python
func.safe_divide(<numerator>, <denominator>, <divide_by_zero_value>)
```

## Analyze 예시

```python
func.safe_divide(table.revenue, table.units, 0)

| revenue | units | safe_divide |
|---------|-------|-------------|
| 100     | 8     | 12.5        |
| 100     | 0     | 0           |
| 100     | NULL  | 0           |
```

```python
func.safe_divide(table.revenue, table.units, None)

| revenue | units | safe_divide |
|---------|-------|-------------|
| 100     | 8     | 12.5        |
| 100     | 0     | NULL        |
```

## SQL 대응 식

이 이름의 SQL 함수는 없습니다. 이 식은 다음과 같이 컴파일됩니다.

```sql
COALESCE(CAST(<numerator> AS DECIMAL(38, 10)) / NULLIF(CAST(<denominator> AS DECIMAL(38, 10)), 0), <divide_by_zero_value>)
```
