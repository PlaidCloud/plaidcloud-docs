---
title: DAYS_DIFF (Lakehouse v2)
description: DAYS_DIFF：返回两个日期之间相差的天数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/days-diff.md
---

返回两个日期之间相差的天数。

## Analyze 语法

```python
func.days_diff(<end_date>, <start_date>)
```

## Analyze 示例

```python
func.days_diff('2024-03-01', '2024-01-01')

┌────┐
│ 60  │
└────┘
```

## SQL 语法

```sql
DAYS_DIFF(<end_date>, <start_date>)
```

## SQL 示例

```sql
SELECT DAYS_DIFF('2024-03-01', '2024-01-01');

┌────┐
│ 60  │
└────┘
```
