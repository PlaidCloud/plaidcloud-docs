---
title: ARRAY_AGG (Lakehouse v2)
description: ARRAY_AGG：将值聚合为数组。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-agg.md
---

将值聚合为数组。

## Analyze 语法

```python
func.array_agg(get_column(table, 'name'))
```

## Analyze 示例

```python
func.array_agg(get_column(table, 'name'))
```

## SQL 语法

```sql
ARRAY_AGG(<name>)
```

## SQL 示例

```sql
SELECT ARRAY_AGG(name) FROM employees;

┌─────────────────────────────┐
│ array_agg(name)             │
├─────────────────────────────┤
│ ["Alice","Bob","Charlie"]   │
└─────────────────────────────┘
```
