---
title: VAR_POP (Lakehouse v2)
description: VAR_POP — 母分散を返します。`VARIANCE_POP` の別名です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/var-pop.md
---

母分散を返します。`VARIANCE_POP` の別名です。

## Analyzeの構文

```python
func.var_pop(get_column(table, 'score'))
```

## Analyzeの例

```python
func.var_pop(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## SQLの構文

```sql
VAR_POP(<score>)
```

## SQLの例

```sql
SELECT VAR_POP(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
