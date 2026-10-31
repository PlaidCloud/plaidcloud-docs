---
title: ANY_VALUE（Lakehouse v2）
description: ANY_VALUE — 行のグループから任意の値を1つ返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/any-value.md
---

行のグループから任意の値を1つ返します。

## Analyzeの構文

```python
func.any_value(get_column(table, 'department'))
```

## Analyzeの例

```python
func.any_value(get_column(table, 'department'))

┌───────┐
│ Sales │
└───────┘
```

## SQLの構文

```sql
ANY_VALUE(<department>)
```

## SQLの例

```sql
SELECT ANY_VALUE(department) FROM employees;

┌───────┐
│ Sales │
└───────┘
```
