---
title: HOURS_ADD (Lakehouse v2)
description: HOURS_ADD：为日期时间加上指定的小时数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hours-add.md
---

为日期时间加上指定的小时数。

## Analyze 语法

```python
func.hours_add(<datetime>, <n>)
```

## Analyze 示例

```python
func.hours_add('2024-01-01 10:00:00', 5)

┌───────────────────────┐
│ '2024-01-01 15:00:00'  │
└───────────────────────┘
```

## SQL 语法

```sql
HOURS_ADD(<datetime>, <n>)
```

## SQL 示例

```sql
SELECT HOURS_ADD('2024-01-01 10:00:00', 5);

┌─────────────────────┐
│ 2024-01-01 15:00:00  │
└─────────────────────┘
```
