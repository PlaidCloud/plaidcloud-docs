---
title: SUBDATE (Lakehouse v2)
description: SUBDATE — 从日期中减去一个时间间隔。是 `DATE_SUB` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/subdate.md
---

从日期中减去一个时间间隔。是 `DATE_SUB` 的别名。

## Analyze 语法

```python
func.subdate(<date>, INTERVAL <n> <unit>)
```

## Analyze 示例

```python
func.subdate('2024-01-31', text('INTERVAL 7 DAY'))

┌──────────────┐
│ '2024-01-24'  │
└──────────────┘
```

## SQL 语法

```sql
SUBDATE(<date>, INTERVAL <n> <unit>)
```

## SQL 示例

```sql
SELECT SUBDATE('2024-01-31', INTERVAL 7 DAY);

┌────────────┐
│ 2024-01-24  │
└────────────┘
```
