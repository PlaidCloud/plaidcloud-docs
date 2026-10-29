---
title: TO_MINUTES (Lakehouse v1)
description: TO_MINUTES — 지정한 분 수를 Interval 형식으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-minutes.md
---

지정한 분 수를 Interval 형식으로 변환합니다.

- 양의 정수, 0, 음의 정수를 입력으로 받습니다.

## Analyze 구문

```python
func.to_minutes(<minutes>)
```

## Analyze 예제

```python
func.to_minutes(2)
┌──────────────────────────────────────────────────────┐
│ func.to_minutes(2)                                   │
├──────────────────────────────────────────────────────┤
│ 0:02:00                                              │
└──────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_MINUTES(<minutes>)
```

## 반환 형식

Interval(`hh:mm:ss` 형식).

## SQL 예제

```sql
SELECT TO_MINUTES(2), TO_MINUTES(0), TO_MINUTES((- 2));

┌─────────────────────────────────────────────────┐
│ to_minutes(2) │ to_minutes(0) │ to_minutes(- 2) │
├───────────────┼───────────────┼─────────────────┤
│ 0:02:00       │ 00:00:00      │ -0:02:00        │
└─────────────────────────────────────────────────┘
```
