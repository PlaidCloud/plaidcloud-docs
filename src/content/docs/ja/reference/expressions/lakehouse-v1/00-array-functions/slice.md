---
title: SLICE (Lakehouse v1)
description: SLICE — インデックス（1から始まる）を指定して、配列からスライスを抽出します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/slice.md
---

インデックス（1から始まる）を指定して、配列からスライスを抽出します。

## Analyzeの構文

```python
func.slice( <array>, <start>[, <end>] )
```

## Analyzeの例

```python
func.slice([1, 21, 32, 4], 2, 3)

┌──────────────────────────────────┐
│ func.slice([1, 21, 32, 4], 2, 3) │
├──────────────────────────────────┤
│ [21,32]                          │ 
└──────────────────────────────────┘
```

## SQLの構文

```sql
SLICE( <array>, <start>[, <end>] )
```

## エイリアス

- [ARRAY_SLICE](../array-slice)

## SQLの例

```sql
SELECT ARRAY_SLICE([1, 21, 32, 4], 2, 3), SLICE([1, 21, 32, 4], 2, 3);

┌─────────────────────────────────────────────────────────────────┐
│ array_slice([1, 21, 32, 4], 2, 3) │ slice([1, 21, 32, 4], 2, 3) │
├───────────────────────────────────┼─────────────────────────────┤
│ [21,32]                           │ [21,32]                     │
└─────────────────────────────────────────────────────────────────┘
```
