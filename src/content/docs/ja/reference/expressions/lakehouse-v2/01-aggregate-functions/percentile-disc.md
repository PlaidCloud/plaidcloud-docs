---
title: "PERCENTILE_DISC (集計, Lakehouse v2)"
description: "PlaidCloud Lakehouse で PERCENTILE_DISC 集計関数を使用します。累積分布が指定したパーセンタイル以上となる最小の値を返します。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-disc.md
---

累積分布が指定したパーセンタイル以上となる最小の値を返します。

## Analyzeの構文

```python
func.percentile_disc(0.5)
```

## Analyzeの例

```python
func.percentile_disc(0.5)

┌───────┐
│ 72000 │
└───────┘
```

## SQLの構文

```sql
PERCENTILE_DISC(0.5)
```

## SQLの例

```sql
SELECT PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000 │
└───────┘
```
