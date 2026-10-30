---
title: NOW (Lakehouse v2)
description: NOW — 현재 날짜와 시간을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/now.md
---

현재 날짜와 시간을 반환합니다.

## Analyze 구문

```python
func.now()
```

## Analyze 예제

```python
func.now()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQL 구문

```sql
NOW()
```

## SQL 예제

```sql
SELECT NOW();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
