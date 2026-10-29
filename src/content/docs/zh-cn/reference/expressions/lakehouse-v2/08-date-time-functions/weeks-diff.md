---
title: WEEKS_DIFF (Lakehouse v2)
description: WEEKS_DIFF — 返回两个日期之间相差的周数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weeks-diff.md
---

返回两个日期之间相差的周数。

## Analyze 语法

```python
func.weeks_diff(<end_date>, <start_date>)
```

## Analyze 示例

```python
func.weeks_diff('2024-03-01', '2024-01-01')

┌───┐
│ 8  │
└───┘
```

## SQL 语法

```sql
WEEKS_DIFF(<end_date>, <start_date>)
```

## SQL 示例

```sql
SELECT WEEKS_DIFF('2024-03-01', '2024-01-01');

┌───┐
│ 8  │
└───┘
```
