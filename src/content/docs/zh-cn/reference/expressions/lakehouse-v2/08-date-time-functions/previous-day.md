---
title: PREVIOUS_DAY (Lakehouse v2)
description: PREVIOUS_DAY — 返回给定日期之前的上一个指定星期几的日期。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/previous-day.md
---

返回给定日期之前的上一个指定星期几的日期。

## Analyze 语法

```python
func.previous_day(<date>, <weekday>)
```

## Analyze 示例

```python
func.previous_day('2024-06-15', 'Monday')

┌──────────────┐
│ '2024-06-10'  │
└──────────────┘
```

## SQL 语法

```sql
PREVIOUS_DAY(<date>, <weekday>)
```

## SQL 示例

```sql
SELECT PREVIOUS_DAY('2024-06-15', 'Monday');

┌────────────┐
│ 2024-06-10  │
└────────────┘
```
