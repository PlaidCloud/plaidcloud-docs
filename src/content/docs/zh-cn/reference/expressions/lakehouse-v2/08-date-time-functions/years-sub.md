---
title: YEARS_SUB (Lakehouse v2)
description: YEARS_SUB — 从日期中减去指定的年数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/years-sub.md
---

从日期中减去指定的年数。

## Analyze 语法

```python
func.years_sub(<date>, <n>)
```

## Analyze 示例

```python
func.years_sub('2029-01-01', 5)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## SQL 语法

```sql
YEARS_SUB(<date>, <n>)
```

## SQL 示例

```sql
SELECT YEARS_SUB('2029-01-01', 5);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
