---
title: PERCENTILE_HASH (Lakehouse v2)
description: PERCENTILE_HASH — 数値からパーセンタイル状態を計算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-hash.md
---

数値からパーセンタイル状態を計算します。

## Analyzeの構文

```python
func.percentile_hash(<value>)
```

## Analyzeの例

```python
func.percentile_hash(42.5)

┌─────────┐
│ (state)  │
└─────────┘
```

## SQLの構文

```sql
PERCENTILE_HASH(<value>)
```

## SQLの例

```sql
SELECT PERCENTILE_HASH(42.5);

┌────────────────────┐
│ (percentile state)  │
└────────────────────┘
```
