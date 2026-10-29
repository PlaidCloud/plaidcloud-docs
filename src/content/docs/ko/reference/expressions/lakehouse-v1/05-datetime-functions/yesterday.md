---
title: YESTERDAY (Lakehouse v1)
description: YESTERDAY — 어제 날짜를 반환하며, today() - 1과 같습니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/yesterday.md
---

어제 날짜를 반환하며, `today() - 1`과 같습니다.

## Analyze 구문

```python
func.yesterday()
```

## Analyze 예제

```python
func.yesterday()
┌──────────────────┐
│ func.yesterday() │
├──────────────────┤
│ 2021-09-02       │
└──────────────────┘
```

## SQL 구문

```sql
YESTERDAY()
```

## 반환 형식

`DATE`, “YYYY-MM-DD” 형식의 날짜를 반환합니다.

## SQL 예제

```sql
SELECT YESTERDAY();
┌─────────────┐
│ YESTERDAY() │
├─────────────┤
│ 2021-09-02  │
└─────────────┘

SELECT TODAY()-1;
┌───────────────┐
│ (TODAY() - 1) │
├───────────────┤
│ 2021-09-02    │
└───────────────┘
```
