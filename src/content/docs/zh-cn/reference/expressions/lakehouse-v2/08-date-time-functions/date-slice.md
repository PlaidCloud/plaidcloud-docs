---
title: DATE_SLICE (Lakehouse v2)
description: "在 PlaidCloud Lakehouse 中使用 DATE_SLICE 日期时间函数。根据指定的周期，将给定时间转换为时间间隔的起点或终点。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-slice.md
---

根据指定的周期，将给定时间转换为时间间隔的起点或终点。

## Analyze 语法

```python
func.date_slice(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## Analyze 示例

```python
func.date_slice('2024-06-15 14:35:00', text('INTERVAL 1 HOUR'))

┌───────────────────────┐
│ '2024-06-15 14:00:00'  │
└───────────────────────┘
```

## SQL 语法

```sql
DATE_SLICE(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## SQL 示例

```sql
SELECT DATE_SLICE('2024-06-15 14:35:00', INTERVAL 1 HOUR);

┌─────────────────────┐
│ 2024-06-15 14:00:00  │
└─────────────────────┘
```
