---
title: BITMAP_CONTAINS (Lakehouse v1)
description: BITMAP_CONTAINS — ビットマップに特定の値が含まれているかどうかを確認します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-contains.md
---

ビットマップに特定の値が含まれているかどうかを確認します。


## Analyzeの構文

```python
func.bitmap_contains( <bitmap>, <value> )
```

## Analyzeの例

```python
func.bitmap_contains(build_bitmap([1, 4, 5]), 1)

┌───────────────────────────────────────────────────┐
│ func.bitmap_contains(build_bitmap([1, 4, 5]), 1)  │
├───────────────────────────────────────────────────┤
│ true                                              │
└───────────────────────────────────────────────────┘
```

## SQLの構文

```sql
BITMAP_CONTAINS( <bitmap>, <value> )
```

## SQLの例

```sql
SELECT BITMAP_CONTAINS(BUILD_BITMAP([1,4,5]), 1);

┌─────────────────────────────────────────────┐
│ bitmap_contains(build_bitmap([1, 4, 5]), 1) │
├─────────────────────────────────────────────┤
│ true                                        │
└─────────────────────────────────────────────┘
```
