---
title: DATE_ADD (Lakehouse v2)
description: DATE_ADD：为日期或日期时间加上指定的时间间隔。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-add.md
---

为日期或日期时间加上指定的时间间隔。

## Analyze 语法

```python
func.date_add(<date>, INTERVAL <n> <unit>)
```

## Analyze 示例

```python
func.date_add('2024-01-01', text('INTERVAL 30 DAY'))

┌──────────────┐
│ '2024-01-31'  │
└──────────────┘
```

## SQL 语法

```sql
DATE_ADD(<date>, INTERVAL <n> <unit>)
```

## SQL 示例

```sql
SELECT DATE_ADD('2024-01-01', INTERVAL 30 DAY);

┌────────────┐
│ 2024-01-31  │
└────────────┘
```
