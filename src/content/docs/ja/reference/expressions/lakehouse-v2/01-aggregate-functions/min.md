---
title: MIN (Lakehouse v2)
description: MIN — 値の集合から最小値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/min.md
---

値の集合から最小値を返します。

## Analyzeの構文

```python
func.min(get_column(table, 'salary'))
```

## Analyzeの例

```python
func.min(get_column(table, 'salary'))

┌───────┐
│ 35000 │
└───────┘
```

## SQLの構文

```sql
MIN(<salary>)
```

## SQLの例

```sql
SELECT MIN(salary) FROM employees;

┌───────┐
│ 35000 │
└───────┘
```
