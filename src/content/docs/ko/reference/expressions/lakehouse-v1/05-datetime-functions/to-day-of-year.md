---
title: TO_DAY_OF_YEAR (Lakehouse v1)
description: TO_DAY_OF_YEAR — 날짜 또는 날짜/시간(타임스탬프/datetime)을 UInt16 숫자로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-day-of-year.md
---

날짜 또는 날짜/시간(타임스탬프/datetime)을 연중 일 번호(1-366)를 담은 UInt16 숫자로 변환합니다.

## Analyze 구문

```python
func.to_day_of_year(<expr>)
```

## Analyze 예시

```python
func.to_day_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_day_of_year('2023-11-12 09:38:18.165575')  │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                316 │
└────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_DAY_OF_YEAR(<expr>)
```

## 인수

| 인수   | 설명 |
| ----------- | ----------- |
| `<expr>` | 날짜/타임스탬프 |

## 반환 형식

`SMALLINT`

## SQL 예시

```sql
SELECT
    to_day_of_year('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ to_day_of_year('2023-11-12 09:38:18.165575') │
│                    UInt16                    │
├──────────────────────────────────────────────┤
│                                          316 │
└──────────────────────────────────────────────┘
```
