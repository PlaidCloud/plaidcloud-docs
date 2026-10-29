---
title: YEARWEEK (Lakehouse v2)
description: YEARWEEK — 以整数形式返回日期的年份和周数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/yearweek.md
---

以整数形式返回日期的年份和周数。

## Analyze 语法

```python
func.yearweek(<date>[, <mode>])
```

## Analyze 示例

```python
func.yearweek('2024-06-15')

┌────────┐
│ 202424  │
└────────┘
```

## SQL 语法

```sql
YEARWEEK(<date>[, <mode>])
```

## SQL 示例

```sql
SELECT YEARWEEK('2024-06-15');

┌────────┐
│ 202424  │
└────────┘
```
