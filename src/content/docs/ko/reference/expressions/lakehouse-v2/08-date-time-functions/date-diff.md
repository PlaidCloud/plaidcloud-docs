---
title: DATE_DIFF (Lakehouse v2)
description: DATE_DIFF — 두 날짜 사이의 차이를 지정한 단위로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-diff.md
---

두 날짜 사이의 차이를 지정한 단위로 반환합니다.

## Analyze 구문

```python
func.date_diff(<unit>, <start>, <end>)
```

## Analyze 예제

```python
func.date_diff('DAY', '2024-01-01', '2024-03-01')

┌────┐
│ 60  │
└────┘
```

## SQL 구문

```sql
DATE_DIFF(<unit>, <start>, <end>)
```

## SQL 예제

```sql
SELECT DATE_DIFF('DAY', '2024-01-01', '2024-03-01');

┌────┐
│ 60  │
└────┘
```
