---
title: TO_ISO8601 (Lakehouse v2)
description: TO_ISO8601 — 날짜 또는 날짜/시간 값을 ISO 8601 형식의 문자열로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-iso8601.md
---

날짜 또는 날짜/시간 값을 ISO 8601 형식의 문자열로 변환합니다.

## Analyze 구문

```python
func.to_iso8601(<datetime>)
```

## Analyze 예제

```python
func.to_iso8601('2024-06-15 14:30:00')

┌───────────────────────┐
│ '2024-06-15T14:30:00'  │
└───────────────────────┘
```

## SQL 구문

```sql
TO_ISO8601(<datetime>)
```

## SQL 예제

```sql
SELECT TO_ISO8601('2024-06-15 14:30:00');

┌─────────────────────┐
│ 2024-06-15T14:30:00  │
└─────────────────────┘
```
