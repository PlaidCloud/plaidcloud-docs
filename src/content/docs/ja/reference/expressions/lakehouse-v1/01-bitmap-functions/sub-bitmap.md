---
title: SUB_BITMAP (Lakehouse v1)
description: SUB_BITMAP — 開始インデックスから指定したサイズのサブビットマップを、元のビットマップから生成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/sub-bitmap.md
---

開始インデックスから指定したサイズのサブビットマップを、元のビットマップから生成します。

## Analyzeの構文

```python
func.sub_bitmap( <bitmap>, <start>, <size> )
```

## Analyzeの例

```python
func.sub_bitmap(func.build_bitmap([1, 2, 3, 4, 5]), 1, 3)

┌───────────────────────────────────────────────────────────┐
│ func.sub_bitmap(func.build_bitmap([1, 2, 3, 4, 5]), 1, 3) │
├───────────────────────────────────────────────────────────┤
│ 2,3,4                                                     │
└───────────────────────────────────────────────────────────┘
```

## SQLの構文

```sql
SUB_BITMAP( <bitmap>, <start>, <size> )
```

## SQLの例

```sql
SELECT SUB_BITMAP(BUILD_BITMAP([1, 2, 3, 4, 5]), 1, 3)::String;

┌─────────────────────────────────────────────────────────┐
│ sub_bitmap(build_bitmap([1, 2, 3, 4, 5]), 1, 3)::string │
├─────────────────────────────────────────────────────────┤
│ 2,3,4                                                   │
└─────────────────────────────────────────────────────────┘
```
