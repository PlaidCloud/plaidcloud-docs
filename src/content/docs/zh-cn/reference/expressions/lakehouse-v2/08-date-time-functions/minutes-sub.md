---
title: MINUTES_SUB (Lakehouse v2)
description: MINUTES_SUB — 从日期时间值中减去指定的分钟数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-sub.md
---

从日期时间值中减去指定的分钟数。

## Analyze 语法

```python
func.minutes_sub(<datetime>, <n>)
```

## Analyze 示例

```python
func.minutes_sub('2024-01-01 10:45:00', 45)

┌───────────────────────┐
│ '2024-01-01 10:00:00'  │
└───────────────────────┘
```

## SQL 语法

```sql
MINUTES_SUB(<datetime>, <n>)
```

## SQL 示例

```sql
SELECT MINUTES_SUB('2024-01-01 10:45:00', 45);

┌─────────────────────┐
│ 2024-01-01 10:00:00  │
└─────────────────────┘
```
