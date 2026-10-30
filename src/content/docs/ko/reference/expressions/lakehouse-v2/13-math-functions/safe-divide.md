---
title: SAFE_DIVIDE (Lakehouse v2)
description: SAFE_DIVIDE — 두 숫자를 나누며, 분모가 0일 때 오류가 발생하는 대신 사용자가 지정한 값을 반환하는 PlaidCloud 함수입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/safe-divide.md
---

모든 Lakehouse 엔진에서 사용할 수 있는 PlaidCloud 함수입니다. 첫 번째 숫자를 두 번째 숫자로 나눕니다. 분모가 0이거나 어느 한쪽이 NULL이면 결과는 NULL이며, 세 번째 값을 지정한 경우에는 그 값을 대신 반환합니다. 정수 열도 잘림 없이 나눌 수 있도록 양쪽을 먼저 `DECIMAL(38, 10)`으로 캐스팅합니다.

## Analyze 구문

```python
func.safe_divide(<numerator>, <denominator>, <divide_by_zero_value>)

func.safe_divide(<numerator>, <denominator>)
```

## Analyze 예제

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

## SQL 대응 구문

이 이름의 SQL 함수는 없습니다. 식은 다음과 같이 컴파일됩니다.

```sql
COALESCE(CAST(<numerator> AS DECIMAL(38, 10)) / NULLIF(CAST(<denominator> AS DECIMAL(38, 10)), 0), <divide_by_zero_value>)
```

세 번째 인수가 없으면 COALESCE가 없으며, 분모가 0일 때 결과는 NULL입니다.

```sql
CAST(<numerator> AS DECIMAL(38, 10)) / NULLIF(CAST(<denominator> AS DECIMAL(38, 10)), 0)
```
