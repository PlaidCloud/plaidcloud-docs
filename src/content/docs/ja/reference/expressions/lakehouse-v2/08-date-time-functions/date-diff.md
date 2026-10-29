---
title: DATE_DIFF (Lakehouse v2)
description: DATE_DIFF — 2 つの日付の差を、指定した単位で返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-diff.md
---

2 つの日付の差を、指定した単位で返します。

## Analyzeの構文

```python
func.date_diff(<unit>, <start>, <end>)
```

## Analyzeの例

```python
func.date_diff('DAY', '2024-01-01', '2024-03-01')

┌────┐
│ 60  │
└────┘
```

## SQLの構文

```sql
DATE_DIFF(<unit>, <start>, <end>)
```

## SQLの例

```sql
SELECT DATE_DIFF('DAY', '2024-01-01', '2024-03-01');

┌────┐
│ 60  │
└────┘
```
