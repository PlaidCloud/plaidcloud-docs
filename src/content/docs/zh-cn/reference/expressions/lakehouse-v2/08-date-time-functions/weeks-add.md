---
title: WEEKS_ADD (Lakehouse v2)
description: WEEKS_ADD — 为日期加上指定的周数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weeks-add.md
---

为日期加上指定的周数。

## Analyze 语法

```python
func.weeks_add(<date>, <n>)
```

## Analyze 示例

```python
func.weeks_add('2024-01-01', 2)

┌──────────────┐
│ '2024-01-15'  │
└──────────────┘
```

## SQL 语法

```sql
WEEKS_ADD(<date>, <n>)
```

## SQL 示例

```sql
SELECT WEEKS_ADD('2024-01-01', 2);

┌────────────┐
│ 2024-01-15  │
└────────────┘
```
