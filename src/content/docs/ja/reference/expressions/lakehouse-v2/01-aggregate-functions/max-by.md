---
title: MAX_BY (Lakehouse v2)
description: MAX_BY — 別の列の最大値に対応する列の値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/max-by.md
---

別の列の最大値に対応する列の値を返します。

## Analyzeの構文

```python
func.max_by(get_column(table, 'name'), get_column(table, 'salary'))
```

## Analyzeの例

```python
func.max_by(get_column(table, 'name'), get_column(table, 'salary'))

┌───────┐
│ Alice │
└───────┘
```

## SQLの構文

```sql
MAX_BY(<name>, <salary>)
```

## SQLの例

```sql
SELECT MAX_BY(name, salary) FROM employees;

┌───────┐
│ Alice │
└───────┘
```
