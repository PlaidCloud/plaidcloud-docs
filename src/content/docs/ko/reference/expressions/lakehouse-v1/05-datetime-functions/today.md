---
title: TODAY (Lakehouse v1)
description: TODAY — 현재 날짜를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/today.md
---

현재 날짜를 반환합니다.

## Analyze 구문

```python
func.today()
```

## Analyze 예제

```python
func.today()
┌──────────────┐
│ func.today() │
├──────────────┤
│ 2021-09-03   │
└──────────────┘
```

## SQL 구문

```sql
TODAY()
```

## 반환 형식

`DATE`, “YYYY-MM-DD” 형식의 날짜를 반환합니다.

## SQL 예제

```sql
SELECT TODAY();
┌────────────┐
│ TODAY()    │
├────────────┤
│ 2021-09-03 │
└────────────┘
```
