---
title: COVAR_POP（Lakehouse v2）
description: COVAR_POP — 2つの式の母共分散を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/covar-pop.md
---

2つの式の母共分散を返します。

## Analyzeの構文

```python
func.covar_pop(get_column(table, 'y'), get_column(table, 'x'))
```

## Analyzeの例

```python
func.covar_pop(get_column(table, 'height'), get_column(table, 'weight'))

┌────────┐
│ 102.46 │
└────────┘
```

## SQLの構文

```sql
COVAR_POP(<y>, <x>)
```

## SQLの例

```sql
SELECT COVAR_POP(height, weight) FROM measurements;

┌────────┐
│ 102.46 │
└────────┘
```
