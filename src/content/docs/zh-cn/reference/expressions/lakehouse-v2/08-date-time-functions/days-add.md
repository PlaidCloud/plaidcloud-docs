---
title: DAYS_ADD (Lakehouse v2)
description: DAYS_ADD：为日期加上指定的天数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/days-add.md
---

为日期加上指定的天数。

## Analyze 语法

```python
func.days_add(<date>, <n>)
```

## Analyze 示例

```python
func.days_add('2024-01-01', 30)

┌──────────────┐
│ '2024-01-31'  │
└──────────────┘
```

## SQL 语法

```sql
DAYS_ADD(<date>, <n>)
```

## SQL 示例

```sql
SELECT DAYS_ADD('2024-01-01', 30);

┌────────────┐
│ 2024-01-31  │
└────────────┘
```
