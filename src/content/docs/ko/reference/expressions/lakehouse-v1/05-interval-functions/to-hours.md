---
title: TO_HOURS (Lakehouse v1)
description: TO_HOURS — 지정한 시간 수를 Interval 형식으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-hours.md
---

지정한 시간 수를 Interval 형식으로 변환합니다.

- 양의 정수, 0, 음의 정수를 입력으로 받습니다.

## Analyze 구문

```python
func.to_hours(<hours>)
```

## Analyze 예제

```python
func.to_hours(2)
┌──────────────────────────────────────────────────────┐
│ func.to_hours(2)                                     │
├──────────────────────────────────────────────────────┤
│ 2:00:00                                              │
└──────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_HOURS(<hours>)
```

## 반환 형식

Interval(`hh:mm:ss` 형식).

## SQL 예제

```sql
SELECT TO_HOURS(2), TO_HOURS(0), TO_HOURS((- 2));

┌───────────────────────────────────────────┐
│ to_hours(2) │ to_hours(0) │ to_hours(- 2) │
├─────────────┼─────────────┼───────────────┤
│ 2:00:00     │ 00:00:00    │ -2:00:00      │
└───────────────────────────────────────────┘
```
