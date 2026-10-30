---
title: VAR_SAMP (Lakehouse v2)
description: VAR_SAMP — 標本分散を返します。`VARIANCE_SAMP` の別名です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/var-samp.md
---

標本分散を返します。`VARIANCE_SAMP` の別名です。

## Analyzeの構文

```python
func.var_samp(get_column(table, 'score'))
```

## Analyzeの例

```python
func.var_samp(get_column(table, 'score'))

┌────────┐
│ 252.48 │
└────────┘
```

## SQLの構文

```sql
VAR_SAMP(<score>)
```

## SQLの例

```sql
SELECT VAR_SAMP(score) FROM test_results;

┌────────┐
│ 252.48 │
└────────┘
```
