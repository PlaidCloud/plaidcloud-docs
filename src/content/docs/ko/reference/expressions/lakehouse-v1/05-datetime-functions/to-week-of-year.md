---
title: TO_WEEK_OF_YEAR (Lakehouse v1)
description: TO_WEEK_OF_YEAR — 지정한 날짜의 연중 주 번호를 계산합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-week-of-year.md
---

지정한 날짜의 연중 주 번호를 계산합니다.

ISO 주 번호는 다음과 같이 부여합니다. 1월 4일은 항상 첫 번째 주에 속합니다. 1월 1일이 목요일이면 12월 29일 월요일부터 1월 4일 일요일까지의 주가 ISO 1주가 됩니다. 1월 1일이 금요일이면 1월 4일 월요일부터 1월 10일 일요일까지의 주가 ISO 1주가 됩니다.

## Analyze 구문

```python
func.to_week_of_year(<expr>)
```

## Analyze 예제

```python
func.now(), func.to_week_of_year(func.now()), func.week(func.now()), func.weekofyear(func.now())

┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_week_of_year(func.now()) │ func.week(func.now()) │ func.weekofyear(func.now()) │
├────────────────────────────┼──────────────────────────────────┼───────────────────────┼─────────────────────────────┤
│ 2024-03-14 23:30:04.011624 │                               11 │                    11 │                          11 │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_WEEK_OF_YEAR(<expr>)
```

## 인수

| 인수 | 설명 |
|-----------|----------------|
| `<expr>`  | date/timestamp |

## 별칭

- [WEEK](../week)
- [WEEKOFYEAR](../weekofyear)

## 반환 형식

연중 주 번호를 나타내는 정수를 반환하며, 번호 범위는 1에서 53까지입니다.

## SQL 예제

```sql
SELECT NOW(), TO_WEEK_OF_YEAR(NOW()), WEEK(NOW()), WEEKOFYEAR(NOW());

┌───────────────────────────────────────────────────────────────────────────────────────┐
│            now()           │ to_week_of_year(now()) │ week(now()) │ weekofyear(now()) │
├────────────────────────────┼────────────────────────┼─────────────┼───────────────────┤
│ 2024-03-14 23:30:04.011624 │                     11 │          11 │                11 │
└───────────────────────────────────────────────────────────────────────────────────────┘
```
