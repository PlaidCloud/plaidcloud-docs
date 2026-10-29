---
title: STDDEV (Lakehouse v2)
description: STDDEV — 母標準偏差を返します。`STDDEV_POP` の別名です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/stddev.md
---

母標準偏差を返します。`STDDEV_POP` の別名です。

## Analyzeの構文

```python
func.stddev(get_column(table, 'score'))
```

## Analyzeの例

```python
func.stddev(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## SQLの構文

```sql
STDDEV(<score>)
```

## SQLの例

```sql
SELECT STDDEV(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
