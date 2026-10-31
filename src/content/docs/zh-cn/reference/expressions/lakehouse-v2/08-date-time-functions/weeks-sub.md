---
title: WEEKS_SUB (Lakehouse v2)
description: WEEKS_SUB — 从日期中减去指定的周数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weeks-sub.md
---

从日期中减去指定的周数。

## Analyze 语法

```python
func.weeks_sub(<date>, <n>)
```

## Analyze 示例

```python
func.weeks_sub('2024-01-15', 2)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## SQL 语法

```sql
WEEKS_SUB(<date>, <n>)
```

## SQL 示例

```sql
SELECT WEEKS_SUB('2024-01-15', 2);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
