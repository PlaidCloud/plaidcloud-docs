---
title: TO_BITMAP (Lakehouse v2)
description: TO_BITMAP — 整数値を、その 1 つの値だけを含むビットマップに変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/to-bitmap.md
---

整数値を、その 1 つの値だけを含むビットマップに変換します。

## Analyzeの構文

```python
func.to_bitmap(<value>)
```

## Analyzeの例

```python
func.to_bitmap(42)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQLの構文

```sql
TO_BITMAP(<value>)
```

## SQLの例

```sql
SELECT BITMAP_TO_STRING(TO_BITMAP(42));

┌────┐
│ 42 │
└────┘
```
