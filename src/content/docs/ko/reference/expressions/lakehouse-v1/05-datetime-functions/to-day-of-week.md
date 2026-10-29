---
title: TO_DAY_OF_WEEK (Lakehouse v1)
description: TO_DAY_OF_WEEK — 날짜 또는 날짜/시간(타임스탬프/datetime)을 UInt8 숫자로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-day-of-week.md
---

날짜 또는 날짜/시간(타임스탬프/datetime)을 요일 번호(월요일은 1, 일요일은 7)를 담은 UInt8 숫자로 변환합니다.

## Analyze 구문

```python
func.to_day_of_week(<expr>)
```

## Analyze 예시

```python
func.to_day_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_day_of_week('2023-11-12 09:38:18.165575')  │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                  7 │
└────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_DAY_OF_WEEK(<expr>)
```

## 인수

| 인수 | 설명    |
|-----------|----------------|
| `<expr>`  | 날짜/타임스탬프 |

## 반환 형식

``TINYINT`

## SQL 예시

```sql

SELECT
    to_day_of_week('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ to_day_of_week('2023-11-12 09:38:18.165575') │
│                     UInt8                    │
├──────────────────────────────────────────────┤
│                                            7 │
└──────────────────────────────────────────────┘
```
