---
title: TO_DAY_OF_MONTH (Lakehouse v1)
description: TO_DAY_OF_MONTH — 날짜 또는 날짜/시간(타임스탬프/datetime)을 UInt8 숫자로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-day-of-month.md
---

날짜 또는 날짜/시간(타임스탬프/datetime)을 월의 일 번호(1-31)를 담은 UInt8 숫자로 변환합니다.

## Analyze 구문

```python
func.to_day_of_month(<expr>)
```

## Analyze 예시

```python
func.now(), func.to_day_of_month(func.now()), func.day(func.now())

┌──────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_day_of_month(func.now()) │ func.day(func.now()) │
├────────────────────────────┼──────────────────────────────────┼──────────────────────┤
│ 2024-03-14 23:35:41.947962 │                               14 │                   14 │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_DAY_OF_MONTH(<expr>)
```

## 인수

| 인수 | 설명    |
|-----------|----------------|
| `<expr>`  | 날짜/타임스탬프 |

## 별칭

- [DAY](../day)

## 반환 형식

`TINYINT`

## SQL 예시

```sql
SELECT NOW(), TO_DAY_OF_MONTH(NOW()), DAY(NOW());

┌──────────────────────────────────────────────────────────────────┐
│            now()           │ to_day_of_month(now()) │ day(now()) │
├────────────────────────────┼────────────────────────┼────────────┤
│ 2024-03-14 23:35:41.947962 │                     14 │         14 │
└──────────────────────────────────────────────────────────────────┘
```
