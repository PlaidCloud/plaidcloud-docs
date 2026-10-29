---
title: MILLISECONDS_DIFF (Lakehouse v2)
description: MILLISECONDS_DIFF — 返回两个日期时间值之间相差的毫秒数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/milliseconds-diff.md
---

返回两个日期时间值之间相差的毫秒数。

## Analyze 语法

```python
func.milliseconds_diff(<end>, <start>)
```

## Analyze 示例

```python
func.milliseconds_diff('2024-01-01 00:00:01', '2024-01-01 00:00:00')

┌──────┐
│ 1000  │
└──────┘
```

## SQL 语法

```sql
MILLISECONDS_DIFF(<end>, <start>)
```

## SQL 示例

```sql
SELECT MILLISECONDS_DIFF('2024-01-01 00:00:01', '2024-01-01 00:00:00');

┌──────┐
│ 1000  │
└──────┘
```
