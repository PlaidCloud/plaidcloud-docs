---
title: UNIX_TIMESTAMP (Lakehouse v2)
description: UNIX_TIMESTAMP — 날짜/시간 값을 Unix 타임스탬프로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/unix-timestamp.md
---

날짜/시간 값을 Unix 타임스탬프로 변환합니다.

## Analyze 구문

```python
func.unix_timestamp([<datetime>])
```

## Analyze 예제

```python
func.unix_timestamp('2024-01-01 00:00:00')

┌────────────┐
│ 1704067200  │
└────────────┘
```

## SQL 구문

```sql
UNIX_TIMESTAMP([<datetime>])
```

## SQL 예제

```sql
SELECT UNIX_TIMESTAMP('2024-01-01 00:00:00');

┌────────────┐
│ 1704067200  │
└────────────┘
```
