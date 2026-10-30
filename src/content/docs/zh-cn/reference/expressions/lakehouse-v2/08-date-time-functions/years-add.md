---
title: YEARS_ADD (Lakehouse v2)
description: YEARS_ADD — 为日期加上指定的年数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/years-add.md
---

为日期加上指定的年数。

## Analyze 语法

```python
func.years_add(<date>, <n>)
```

## Analyze 示例

```python
func.years_add('2024-01-01', 5)

┌──────────────┐
│ '2029-01-01'  │
└──────────────┘
```

## SQL 语法

```sql
YEARS_ADD(<date>, <n>)
```

## SQL 示例

```sql
SELECT YEARS_ADD('2024-01-01', 5);

┌────────────┐
│ 2029-01-01  │
└────────────┘
```
