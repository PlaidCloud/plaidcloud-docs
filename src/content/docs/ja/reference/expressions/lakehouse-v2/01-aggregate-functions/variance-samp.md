---
title: VARIANCE_SAMP (Lakehouse v2)
description: VARIANCE_SAMP — 標本分散を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/variance-samp.md
---

標本分散を返します。

## Analyzeの構文

```python
func.variance_samp(get_column(table, 'score'))
```

## Analyzeの例

```python
func.variance_samp(get_column(table, 'score'))

┌────────┐
│ 252.48 │
└────────┘
```

## SQLの構文

```sql
VARIANCE_SAMP(<score>)
```

## SQLの例

```sql
SELECT VARIANCE_SAMP(score) FROM test_results;

┌────────┐
│ 252.48 │
└────────┘
```
