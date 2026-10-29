---
title: GENERATE_SERIES（Lakehouse v2）
description: GENERATE_SERIES — 開始値から終了値まで、指定したステップ幅で値の系列を生成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/20-table-functions/generate-series.md
---

開始値から終了値まで、指定したステップ幅で値の系列を生成します。

## Analyze 構文

```python
func.generate_series(<start>, <stop>[, <step>])
```

## Analyze の例

```python
func.generate_series(1, 5)

┌─────────────────┐
│ [1, 2, 3, 4, 5]  │
└─────────────────┘
```

## SQL 構文

```sql
GENERATE_SERIES(<start>, <stop>[, <step>])
```

## SQL の例

```sql
SELECT * FROM TABLE(GENERATE_SERIES(1, 5));

┌───────────┐
│ 1
2
3
4
5  │
└───────────┘
```
