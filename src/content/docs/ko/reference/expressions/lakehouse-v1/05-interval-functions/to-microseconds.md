---
title: TO_MICROSECONDS (Lakehouse v1)
description: TO_MICROSECONDS — 지정한 마이크로초 수를 Interval 형식으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-microseconds.md
---

지정한 마이크로초 수를 Interval 형식으로 변환합니다.

- 양의 정수, 0, 음의 정수를 입력으로 받습니다.

## Analyze 구문

```python
func.to_microseconds(<microseconds>)
```

## Analyze 예제

```python
func.to_microseconds(2)
┌──────────────────────────────────────────────────────┐
│ func.to_microseconds(2)                              │
├──────────────────────────────────────────────────────┤
│ 0:00:00.000002                                       │
└──────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_MICROSECONDS(<microseconds>)
```

## 반환 형식

Interval(`hh:mm:ss.sssssss` 형식).

## SQL 예제

```sql
SELECT TO_MICROSECONDS(2), TO_MICROSECONDS(0), TO_MICROSECONDS((- 2));

┌────────────────────────────────────────────────────────────────┐
│ to_microseconds(2) │ to_microseconds(0) │ to_microseconds(- 2) │
├────────────────────┼────────────────────┼──────────────────────┤
│ 0:00:00.000002     │ 00:00:00           │ -0:00:00.000002      │
└────────────────────────────────────────────────────────────────┘
```
