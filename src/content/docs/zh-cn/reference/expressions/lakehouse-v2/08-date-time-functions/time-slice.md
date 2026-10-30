---
title: TIME_SLICE (Lakehouse v2)
description: TIME_SLICE — 将给定时间转换为所属时间间隔的起点或终点。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/time-slice.md
---

将给定时间转换为所属时间间隔的起点或终点。

## Analyze 语法

```python
func.time_slice(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## Analyze 示例

```python
func.time_slice('2024-06-15 14:35:00', text('INTERVAL 15 MINUTE'))

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQL 语法

```sql
TIME_SLICE(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## SQL 示例

```sql
SELECT TIME_SLICE('2024-06-15 14:35:00', INTERVAL 15 MINUTE);

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
