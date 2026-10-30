---
title: PERCENTILE_EMPTY (Lakehouse v2)
description: PERCENTILE_EMPTY — 初期化用の空のパーセンタイル状態を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-empty.md
---

初期化用の空のパーセンタイル状態を返します。

## Analyzeの構文

```python
func.percentile_empty()
```

## Analyzeの例

```python
func.percentile_empty()

┌───────────────┐
│ (empty state)  │
└───────────────┘
```

## SQLの構文

```sql
PERCENTILE_EMPTY()
```

## SQLの例

```sql
SELECT PERCENTILE_EMPTY();

┌────────────────────┐
│ (percentile state)  │
└────────────────────┘
```
