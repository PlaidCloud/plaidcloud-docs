---
title: DAYS_SUB (Lakehouse v2)
description: DAYS_SUB：从日期中减去指定的天数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/days-sub.md
---

从日期中减去指定的天数。

## Analyze 语法

```python
func.days_sub(<date>, <n>)
```

## Analyze 示例

```python
func.days_sub('2024-01-31', 30)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## SQL 语法

```sql
DAYS_SUB(<date>, <n>)
```

## SQL 示例

```sql
SELECT DAYS_SUB('2024-01-31', 30);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
