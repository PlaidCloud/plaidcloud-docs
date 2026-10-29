---
title: BOOL_OR（Lakehouse v2）
description: BOOL_OR — グループ内にTRUEの値が1つでもあればTRUEを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/bool-or.md
---

グループ内にTRUEの値が1つでもあればTRUEを返します。

## Analyzeの構文

```python
func.bool_or(get_column(table, 'is_active'))
```

## Analyzeの例

```python
func.bool_or(get_column(table, 'is_active'))
```

## SQLの構文

```sql
BOOL_OR(<is_active>)
```

## SQLの例

```sql
SELECT department, BOOL_OR(is_active) FROM employees GROUP BY department;

┌────────────┬─────────────────────┐
│ department │ bool_or(is_active)  │
├────────────┼─────────────────────┤
│ Sales      │                   1 │
│ IT         │                   1 │
└────────────┴─────────────────────┘
```
