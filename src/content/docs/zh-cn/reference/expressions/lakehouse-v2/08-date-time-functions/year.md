---
title: YEAR (Lakehouse v2)
description: YEAR — 返回日期中的年份。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/year.md
---

返回日期中的年份。

## Analyze 语法

```python
func.year(<date>)
```

## Analyze 示例

```python
func.year('2024-06-15')

┌──────┐
│ 2024  │
└──────┘
```

## SQL 语法

```sql
YEAR(<date>)
```

## SQL 示例

```sql
SELECT YEAR('2024-06-15');

┌──────┐
│ 2024  │
└──────┘
```
