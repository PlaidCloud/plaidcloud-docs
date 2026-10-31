---
title: PERCENTILE_DISC_LC (Lakehouse v2)
description: PERCENTILE_DISC_LC — 低カーディナリティ向けに最適化されたアルゴリズムを使用してパーセンタイル値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-disc-lc.md
---

低カーディナリティ向けに最適化されたアルゴリズムを使用してパーセンタイル値を返します。

## Analyzeの構文

```python
func.percentile_disc_lc(0.5)
```

## Analyzeの例

```python
func.percentile_disc_lc(0.5)

┌───────┐
│ 72000 │
└───────┘
```

## SQLの構文

```sql
PERCENTILE_DISC_LC(0.5)
```

## SQLの例

```sql
SELECT PERCENTILE_DISC_LC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000 │
└───────┘
```
