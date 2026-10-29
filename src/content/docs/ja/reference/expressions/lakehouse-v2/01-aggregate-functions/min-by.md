---
title: MIN_BY (Lakehouse v2)
description: MIN_BY — 別の列の最小値に対応する列の値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/min-by.md
---

別の列の最小値に対応する列の値を返します。

## Analyzeの構文

```python
func.min_by(get_column(table, 'name'), get_column(table, 'salary'))
```

## Analyzeの例

```python
func.min_by(get_column(table, 'name'), get_column(table, 'salary'))

┌─────┐
│ Bob │
└─────┘
```

## SQLの構文

```sql
MIN_BY(<name>, <salary>)
```

## SQLの例

```sql
SELECT MIN_BY(name, salary) FROM employees;

┌─────┐
│ Bob │
└─────┘
```
