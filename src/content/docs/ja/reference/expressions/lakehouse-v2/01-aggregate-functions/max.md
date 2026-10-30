---
title: MAX (Lakehouse v2)
description: MAX — 値の集合から最大値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/max.md
---

値の集合から最大値を返します。

## Analyzeの構文

```python
func.max(get_column(table, 'salary'))
```

## Analyzeの例

```python
func.max(get_column(table, 'salary'))

┌────────┐
│ 150000 │
└────────┘
```

## SQLの構文

```sql
MAX(<salary>)
```

## SQLの例

```sql
SELECT MAX(salary) FROM employees;

┌────────┐
│ 150000 │
└────────┘
```
