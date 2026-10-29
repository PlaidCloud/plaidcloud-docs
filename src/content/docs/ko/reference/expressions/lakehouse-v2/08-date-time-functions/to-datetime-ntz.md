---
title: TO_DATETIME_NTZ (Lakehouse v2)
description: TO_DATETIME_NTZ — 값을 시간대가 없는(NTZ) DATETIME으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-datetime-ntz.md
---

값을 시간대가 없는(NTZ) DATETIME으로 변환합니다. 결과는 세션 시간대 설정의 영향을 받지 않습니다.

## Analyze 구문

```python
func.to_datetime_ntz('2024-06-15 14:30:00')
```

## Analyze 예제

```python
func.to_datetime_ntz('2024-06-15 14:30:00')

┌─────────────────────┐
│ 2024-06-15 14:30:00 │
└─────────────────────┘
```

## SQL 구문

```sql
TO_DATETIME_NTZ(<expr>)
```

## SQL 예제

```sql
SELECT TO_DATETIME_NTZ('2024-06-15 14:30:00');

┌─────────────────────┐
│ 2024-06-15 14:30:00 │
└─────────────────────┘
```
