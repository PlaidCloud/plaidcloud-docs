---
title: MONTHS_DIFF (Lakehouse v2)
description: MONTHS_DIFF — 返回两个日期之间相差的月数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/months-diff.md
---

返回两个日期之间相差的月数。

## Analyze 语法

```python
func.months_diff(<end_date>, <start_date>)
```

## Analyze 示例

```python
func.months_diff('2024-06-01', '2024-01-01')

┌───┐
│ 5  │
└───┘
```

## SQL 语法

```sql
MONTHS_DIFF(<end_date>, <start_date>)
```

## SQL 示例

```sql
SELECT MONTHS_DIFF('2024-06-01', '2024-01-01');

┌───┐
│ 5  │
└───┘
```
