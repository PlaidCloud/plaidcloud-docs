---
title: MONTHS_ADD (Lakehouse v2)
description: MONTHS_ADD — 为日期加上指定的月数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/months-add.md
---

为日期加上指定的月数。

## Analyze 语法

```python
func.months_add(<date>, <n>)
```

## Analyze 示例

```python
func.months_add('2024-01-15', 3)

┌──────────────┐
│ '2024-04-15'  │
└──────────────┘
```

## SQL 语法

```sql
MONTHS_ADD(<date>, <n>)
```

## SQL 示例

```sql
SELECT MONTHS_ADD('2024-01-15', 3);

┌────────────┐
│ 2024-04-15  │
└────────────┘
```
