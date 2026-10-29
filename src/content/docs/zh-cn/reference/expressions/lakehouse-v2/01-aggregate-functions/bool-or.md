---
title: BOOL_OR (Lakehouse v2)
description: BOOL_OR：如果组中任一值为 TRUE，则返回 TRUE。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/bool-or.md
---

如果组中任一值为 TRUE，则返回 TRUE。

## Analyze 语法

```python
func.bool_or(get_column(table, 'is_active'))
```

## Analyze 示例

```python
func.bool_or(get_column(table, 'is_active'))
```

## SQL 语法

```sql
BOOL_OR(<is_active>)
```

## SQL 示例

```sql
SELECT department, BOOL_OR(is_active) FROM employees GROUP BY department;

┌────────────┬─────────────────────┐
│ department │ bool_or(is_active)  │
├────────────┼─────────────────────┤
│ Sales      │                   1 │
│ IT         │                   1 │
└────────────┴─────────────────────┘
```
