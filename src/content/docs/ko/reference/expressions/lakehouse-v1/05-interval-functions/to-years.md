---
title: TO_YEARS (Lakehouse v1)
description: TO_YEARS — 지정한 연 수를 Interval 형식으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-years.md
---

지정한 연 수를 Interval 형식으로 변환합니다.

- 양의 정수, 0, 음의 정수를 입력으로 받습니다.

## Analyze 구문

```python
func.to_years(<years>)
```

## Analyze 예제

```python
func.to_years(2)
┌──────────────────────────────────────────────────────┐
│ func.to_years(2)                                     │
├──────────────────────────────────────────────────────┤
│ 2 years                                              │
└──────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_YEARS(<years>)
```

## 반환 형식

Interval(년 단위로 표현).

## SQL 예제

```sql
SELECT TO_YEARS(2), TO_YEARS(0), TO_YEARS((- 2));

┌───────────────────────────────────────────┐
│ to_years(2) │ to_years(0) │ to_years(- 2) │
├─────────────┼─────────────┼───────────────┤
│ 2 years     │ 00:00:00    │ -2 years      │
└───────────────────────────────────────────┘
```
