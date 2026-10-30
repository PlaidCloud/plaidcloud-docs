---
title: DATEDIFF (Lakehouse v2)
description: DATEDIFF：返回两个日期之间相差的天数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/datediff.md
---

返回两个日期之间相差的天数。

## Analyze 语法

```python
func.datediff(<end_date>, <start_date>)
```

## Analyze 示例

```python
func.datediff('2024-03-01', '2024-01-01')

┌────┐
│ 60  │
└────┘
```

## SQL 语法

```sql
DATEDIFF(<end_date>, <start_date>)
```

## SQL 示例

```sql
SELECT DATEDIFF('2024-03-01', '2024-01-01');

┌────┐
│ 60  │
└────┘
```
