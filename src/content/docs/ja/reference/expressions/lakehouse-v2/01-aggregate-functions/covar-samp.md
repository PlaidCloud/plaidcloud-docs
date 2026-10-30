---
title: COVAR_SAMP（Lakehouse v2）
description: COVAR_SAMP — 2つの式の標本共分散を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/covar-samp.md
---

2つの式の標本共分散を返します。

## Analyzeの構文

```python
func.covar_samp(get_column(table, 'y'), get_column(table, 'x'))
```

## Analyzeの例

```python
func.covar_samp(get_column(table, 'height'), get_column(table, 'weight'))

┌────────┐
│ 103.01 │
└────────┘
```

## SQLの構文

```sql
COVAR_SAMP(<y>, <x>)
```

## SQLの例

```sql
SELECT COVAR_SAMP(height, weight) FROM measurements;

┌────────┐
│ 103.01 │
└────────┘
```
