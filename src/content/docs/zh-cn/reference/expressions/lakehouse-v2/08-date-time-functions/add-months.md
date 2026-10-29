---
title: ADD_MONTHS (Lakehouse v2)
description: ADD_MONTHS：为日期加上指定的月数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/add-months.md
---

为日期加上指定的月数。

## Analyze 语法

```python
func.add_months(<date>, <months>)
```

## Analyze 示例

```python
func.add_months('2024-01-31', 1)

┌──────────────┐
│ '2024-02-29'  │
└──────────────┘
```

## SQL 语法

```sql
ADD_MONTHS(<date>, <months>)
```

## SQL 示例

```sql
SELECT ADD_MONTHS('2024-01-31', 1);

┌────────────┐
│ 2024-02-29  │
└────────────┘
```
