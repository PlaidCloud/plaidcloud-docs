---
title: SECONDS_DIFF (Lakehouse v2)
description: SECONDS_DIFF — 返回两个日期时间值之间相差的秒数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-diff.md
---

返回两个日期时间值之间相差的秒数。

## Analyze 语法

```python
func.seconds_diff(<end>, <start>)
```

## Analyze 示例

```python
func.seconds_diff('2024-01-01 00:01:30', '2024-01-01 00:00:00')

┌────┐
│ 90  │
└────┘
```

## SQL 语法

```sql
SECONDS_DIFF(<end>, <start>)
```

## SQL 示例

```sql
SELECT SECONDS_DIFF('2024-01-01 00:01:30', '2024-01-01 00:00:00');

┌────┐
│ 90  │
└────┘
```
