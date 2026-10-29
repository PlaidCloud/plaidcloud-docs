---
title: QUARTER (Lakehouse v2)
description: QUARTER — 返回日期所属的季度（1-4）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/quarter.md
---

返回日期所属的季度（1-4）。

## Analyze 语法

```python
func.quarter(<date>)
```

## Analyze 示例

```python
func.quarter('2024-06-15')

┌───┐
│ 2  │
└───┘
```

## SQL 语法

```sql
QUARTER(<date>)
```

## SQL 示例

```sql
SELECT QUARTER('2024-06-15');

┌───┐
│ 2  │
└───┘
```
