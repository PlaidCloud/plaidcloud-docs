---
title: MAP_KEYS (Lakehouse v2)
description: MAP_KEYS — マップのすべてのキーを配列として返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-keys.md
---

マップのすべてのキーを配列として返します。

## Analyzeの構文

```python
func.map_keys(get_column(table, 'map_col'))
```

## Analyzeの例

```python
func.map_keys(MAP{'a':1,'b':2})

┌───────────┐
│ ['a','b'] │
└───────────┘
```

## SQLの構文

```sql
MAP_KEYS(<map_col>)
```

## SQLの例

```sql
SELECT MAP_KEYS(MAP{'a':1, 'b':2});

┌───────────┐
│ ["a","b"] │
└───────────┘
```
