---
title: YEARS_DIFF (Lakehouse v2)
description: YEARS_DIFF — 返回两个日期之间相差的年数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/years-diff.md
---

返回两个日期之间相差的年数。

## Analyze 语法

```python
func.years_diff(<end_date>, <start_date>)
```

## Analyze 示例

```python
func.years_diff('2029-01-01', '2024-01-01')

┌───┐
│ 5  │
└───┘
```

## SQL 语法

```sql
YEARS_DIFF(<end_date>, <start_date>)
```

## SQL 示例

```sql
SELECT YEARS_DIFF('2029-01-01', '2024-01-01');

┌───┐
│ 5  │
└───┘
```
