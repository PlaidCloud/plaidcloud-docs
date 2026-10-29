---
title: MINUTES_DIFF (Lakehouse v2)
description: MINUTES_DIFF — 返回两个日期时间值之间相差的分钟数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-diff.md
---

返回两个日期时间值之间相差的分钟数。

## Analyze 语法

```python
func.minutes_diff(<end>, <start>)
```

## Analyze 示例

```python
func.minutes_diff('2024-01-01 11:00:00', '2024-01-01 10:00:00')

┌────┐
│ 60  │
└────┘
```

## SQL 语法

```sql
MINUTES_DIFF(<end>, <start>)
```

## SQL 示例

```sql
SELECT MINUTES_DIFF('2024-01-01 11:00:00', '2024-01-01 10:00:00');

┌────┐
│ 60  │
└────┘
```
