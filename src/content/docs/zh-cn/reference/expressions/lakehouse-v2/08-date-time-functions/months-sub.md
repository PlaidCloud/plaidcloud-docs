---
title: MONTHS_SUB (Lakehouse v2)
description: MONTHS_SUB — 从日期中减去指定的月数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/months-sub.md
---

从日期中减去指定的月数。

## Analyze 语法

```python
func.months_sub(<date>, <n>)
```

## Analyze 示例

```python
func.months_sub('2024-06-15', 3)

┌──────────────┐
│ '2024-03-15'  │
└──────────────┘
```

## SQL 语法

```sql
MONTHS_SUB(<date>, <n>)
```

## SQL 示例

```sql
SELECT MONTHS_SUB('2024-06-15', 3);

┌────────────┐
│ 2024-03-15  │
└────────────┘
```
