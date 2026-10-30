---
title: BITMAP_EMPTY (Lakehouse v2)
description: BITMAP_EMPTY — 空のビットマップを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-empty.md
---

空のビットマップを返します。

## Analyzeの構文

```python
func.bitmap_empty()
```

## Analyzeの例

```python
func.bitmap_empty()

┌────────────────┐
│ (empty bitmap) │
└────────────────┘
```

## SQLの構文

```sql
BITMAP_EMPTY()
```

## SQLの例

```sql
SELECT BITMAP_COUNT(BITMAP_EMPTY());

┌───┐
│ 0 │
└───┘
```
