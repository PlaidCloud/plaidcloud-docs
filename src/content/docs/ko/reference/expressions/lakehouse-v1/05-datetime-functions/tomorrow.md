---
title: TOMORROW (Lakehouse v1)
description: TOMORROW — 내일 날짜를 반환하며, today() + 1과 같습니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/tomorrow.md
---

내일 날짜를 반환하며, `today() + 1`과 같습니다.

## Analyze 구문

```python
func.tomorrow()
```

## Analyze 예제

```python
func.tomorrow()
┌─────────────────┐
│ func.tomorrow() │
├─────────────────┤
│ 2021-09-03      │
└─────────────────┘
```

## SQL 구문

```sql
TOMORROW()
```

## 반환 형식

`DATE`, “YYYY-MM-DD” 형식의 날짜를 반환합니다.

## SQL 예제

```sql
SELECT TOMORROW();
┌────────────┐
│ TOMORROW() │
├────────────┤
│ 2021-09-04 │
└────────────┘

SELECT TODAY()+1;
┌───────────────┐
│ (TODAY() + 1) │
├───────────────┤
│ 2021-09-04    │
└───────────────┘
```
