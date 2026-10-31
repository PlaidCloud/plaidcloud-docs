---
title: MAP_FILTER (Lakehouse v2)
description: MAP_FILTER — ラムダ式を使用して、マップ内のキーと値のペアをフィルターします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-filter.md
---

ラムダ式を使用して、マップ内のキーと値のペアをフィルターします。

## Analyzeの構文

```python
func.map_filter(get_column(table, 'map_col'), lambda k, v: v > 1)
```

## Analyzeの例

```python
func.map_filter(MAP{'a':1,'b':2,'c':3}, lambda k,v: v>1)

┌───────────────┐
│ {'b':2,'c':3} │
└───────────────┘
```

## SQLの構文

```sql
MAP_FILTER(<map_col>, lambda k, v: v > 1)
```

## SQLの例

```sql
SELECT MAP_FILTER((k, v) -> v > 1, MAP{'a':1, 'b':2, 'c':3});

┌───────────────┐
│ {"b":2,"c":3} │
└───────────────┘
```
