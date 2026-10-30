---
title: NEXT_DAY (Lakehouse v2)
description: NEXT_DAY — 返回给定日期之后的下一个指定星期几的日期。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/next-day.md
---

返回给定日期之后的下一个指定星期几的日期。

## Analyze 语法

```python
func.next_day(<date>, <weekday>)
```

## Analyze 示例

```python
func.next_day('2024-06-15', 'Monday')

┌──────────────┐
│ '2024-06-17'  │
└──────────────┘
```

## SQL 语法

```sql
NEXT_DAY(<date>, <weekday>)
```

## SQL 示例

```sql
SELECT NEXT_DAY('2024-06-15', 'Monday');

┌────────────┐
│ 2024-06-17  │
└────────────┘
```
