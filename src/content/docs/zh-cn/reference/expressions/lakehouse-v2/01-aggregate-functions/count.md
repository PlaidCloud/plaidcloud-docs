---
title: COUNT (Lakehouse v2)
description: COUNT：返回行数或非 NULL 值的数量。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/count.md
---

返回行数或非 NULL 值的数量。

## Analyze 语法

```python
func.count()
```

## Analyze 示例

```python
func.count()
```

## SQL 语法

```sql
COUNT()
```

## SQL 示例

```sql
SELECT COUNT(*) FROM employees;

┌──────────┐
│ count(*) │
├──────────┤
│     1000 │
└──────────┘

SELECT COUNT(DISTINCT department) FROM employees;

┌──────────────────────────────┐
│ count(distinct department)   │
├──────────────────────────────┤
│                            5 │
└──────────────────────────────┘
```
