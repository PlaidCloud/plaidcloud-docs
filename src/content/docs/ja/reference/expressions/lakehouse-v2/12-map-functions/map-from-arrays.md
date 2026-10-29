---
title: MAP_FROM_ARRAYS (Lakehouse v2)
description: MAP_FROM_ARRAYS — キーの配列と値の配列からマップを作成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-from-arrays.md
---

キーの配列と値の配列からマップを作成します。

## Analyzeの構文

```python
func.map_from_arrays(['a','b'], [1, 2])
```

## Analyzeの例

```python
func.map_from_arrays(['a', 'b', 'c'], [1, 2, 3])

┌─────────────────────┐
│ {'a':1,'b':2,'c':3} │
└─────────────────────┘
```

## SQLの構文

```sql
MAP_FROM_ARRAYS(['a','b'], [1, 2])
```

## SQLの例

```sql
SELECT MAP_FROM_ARRAYS(['a', 'b', 'c'], [1, 2, 3]);

┌─────────────────────┐
│ {"a":1,"b":2,"c":3} │
└─────────────────────┘
```
