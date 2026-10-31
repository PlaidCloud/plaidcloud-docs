---
title: HOURS_SUB (Lakehouse v2)
description: HOURS_SUB：从日期时间中减去指定的小时数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hours-sub.md
---

从日期时间中减去指定的小时数。

## Analyze 语法

```python
func.hours_sub(<datetime>, <n>)
```

## Analyze 示例

```python
func.hours_sub('2024-01-01 15:00:00', 5)

┌───────────────────────┐
│ '2024-01-01 10:00:00'  │
└───────────────────────┘
```

## SQL 语法

```sql
HOURS_SUB(<datetime>, <n>)
```

## SQL 示例

```sql
SELECT HOURS_SUB('2024-01-01 15:00:00', 5);

┌─────────────────────┐
│ 2024-01-01 10:00:00  │
└─────────────────────┘
```
