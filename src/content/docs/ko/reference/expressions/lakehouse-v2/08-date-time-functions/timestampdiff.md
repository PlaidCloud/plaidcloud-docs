---
title: TIMESTAMPDIFF (Lakehouse v2)
description: TIMESTAMPDIFF — 두 날짜/시간 값의 차이를 지정한 단위로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestampdiff.md
---

두 날짜/시간 값의 차이를 지정한 단위로 반환합니다.

## Analyze 구문

```python
func.timestampdiff(<unit>, <start>, <end>)
```

## Analyze 예제

```python
func.timestampdiff('DAY', '2024-01-01', '2024-03-01')

┌────┐
│ 60  │
└────┘
```

## SQL 구문

```sql
TIMESTAMPDIFF(<unit>, <start>, <end>)
```

## SQL 예제

```sql
SELECT TIMESTAMPDIFF(DAY, '2024-01-01', '2024-03-01');

┌────┐
│ 60  │
└────┘
```
