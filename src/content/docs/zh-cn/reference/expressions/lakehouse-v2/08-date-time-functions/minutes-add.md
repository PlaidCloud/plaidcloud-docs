---
title: MINUTES_ADD (Lakehouse v2)
description: MINUTES_ADD — 为日期时间值加上指定的分钟数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-add.md
---

为日期时间值加上指定的分钟数。

## Analyze 语法

```python
func.minutes_add(<datetime>, <n>)
```

## Analyze 示例

```python
func.minutes_add('2024-01-01 10:00:00', 45)

┌───────────────────────┐
│ '2024-01-01 10:45:00'  │
└───────────────────────┘
```

## SQL 语法

```sql
MINUTES_ADD(<datetime>, <n>)
```

## SQL 示例

```sql
SELECT MINUTES_ADD('2024-01-01 10:00:00', 45);

┌─────────────────────┐
│ 2024-01-01 10:45:00  │
└─────────────────────┘
```
