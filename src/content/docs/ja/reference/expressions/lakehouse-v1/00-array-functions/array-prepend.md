---
title: ARRAY_PREPEND (Lakehouse v1)
description: ARRAY_PREPEND — 配列の先頭に要素を追加します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-prepend.md
---

配列の先頭に要素を追加します。

## Analyzeの構文

```python
func.array_prepend( <element>, <array> )
```

## Analyzeの例

```python
func.array_prepend(1, [3, 4])

┌────────────────────────────────┐
│ func.array_prepend(1, [3, 4])  │
├────────────────────────────────┤
│ [1,3,4]                        │
└────────────────────────────────┘
```

## SQLの構文

```sql
ARRAY_PREPEND( <element>, <array> )
```

## SQLの例

```sql
SELECT ARRAY_PREPEND(1, [3, 4]);

┌──────────────────────────┐
│ array_prepend(1, [3, 4]) │
├──────────────────────────┤
│ [1,3,4]                  │
└──────────────────────────┘
```
