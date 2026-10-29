---
title: MAP_APPLY (Lakehouse v2)
description: MAP_APPLY — マップ内の各キーと値のペアにラムダ式を適用します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-apply.md
---

マップ内の各キーと値のペアにラムダ式を適用します。

## Analyzeの構文

```python
func.map_apply(get_column(table, 'map_col'), lambda k, v: (k, v*2))
```

## Analyzeの例

```python
func.map_apply(MAP{'a':1,'b':2}, lambda k,v: (k, v*2))

┌───────────────┐
│ {'a':2,'b':4} │
└───────────────┘
```

## SQLの構文

```sql
MAP_APPLY(<map_col>, lambda k, v: (k, v*2))
```

## SQLの例

```sql
SELECT MAP_APPLY((k, v) -> (k, v * 2), MAP{'a':1, 'b':2});

┌───────────────┐
│ {"a":2,"b":4} │
└───────────────┘
```
