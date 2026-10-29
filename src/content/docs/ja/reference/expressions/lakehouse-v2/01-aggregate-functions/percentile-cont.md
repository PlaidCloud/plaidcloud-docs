---
title: "PERCENTILE_CONT (集計, Lakehouse v2)"
description: PERCENTILE_CONT — 連続分布に基づいて補間したパーセンタイル値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-cont.md
---

連続分布に基づいて補間したパーセンタイル値を返します。

## Analyzeの構文

```python
func.percentile_cont(0.5)
```

## Analyzeの例

```python
func.percentile_cont(0.5)

┌──────────┐
│ 72500.00 │
└──────────┘
```

## SQLの構文

```sql
PERCENTILE_CONT(0.5)
```

## SQLの例

```sql
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌──────────┐
│ 72500.00 │
└──────────┘
```
