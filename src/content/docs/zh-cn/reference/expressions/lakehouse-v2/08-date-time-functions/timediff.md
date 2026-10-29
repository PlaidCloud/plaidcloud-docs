---
title: TIMEDIFF (Lakehouse v2)
description: TIMEDIFF — 返回两个时间值之间的差值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timediff.md
---

返回两个时间值之间的差值。

## Analyze 语法

```python
func.timediff(<time1>, <time2>)
```

## Analyze 示例

```python
func.timediff('15:30:00', '10:00:00')

┌────────────┐
│ '05:30:00'  │
└────────────┘
```

## SQL 语法

```sql
TIMEDIFF(<time1>, <time2>)
```

## SQL 示例

```sql
SELECT TIMEDIFF('15:30:00', '10:00:00');

┌──────────┐
│ 05:30:00  │
└──────────┘
```
