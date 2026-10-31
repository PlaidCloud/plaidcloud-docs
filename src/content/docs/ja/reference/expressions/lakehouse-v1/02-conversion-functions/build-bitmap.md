---
title: BUILD_BITMAP (Lakehouse v1)
description: BUILD_BITMAP — 正の整数の配列をBITMAP値に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/build-bitmap.md
---

正の整数の配列をBITMAP値に変換します。


## Analyzeの構文

```python
func.build_bitmap( <expr> )
```

## Analyzeの例

```python
func.to_string(func.build_bitmap([1, 4, 5]))

┌───────────────────────────────────────────────┐
│ func.to_string(func.build_bitmap([1, 4, 5]))  │
├───────────────────────────────────────────────┤
│ 1,4,5                                         │
└───────────────────────────────────────────────┘
```

## SQLの構文

```sql
BUILD_BITMAP( <expr> )
```

## SQLの例

```sql
SELECT BUILD_BITMAP([1,4,5])::String;

┌─────────────────────────────────┐
│ build_bitmap([1, 4, 5])::string │
├─────────────────────────────────┤
│ 1,4,5                           │
└─────────────────────────────────┘
```
