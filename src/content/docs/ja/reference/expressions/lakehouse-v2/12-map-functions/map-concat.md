---
title: MAP_CONCAT (Lakehouse v2)
description: MAP_CONCAT — 複数のマップを1つのマップに連結します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-concat.md
---

複数のマップを1つのマップに連結します。

## Analyzeの構文

```python
func.map_concat(map1, map2)
```

## Analyzeの例

```python
func.map_concat(MAP{'a':1}, MAP{'b':2})

┌───────────────┐
│ {'a':1,'b':2} │
└───────────────┘
```

## SQLの構文

```sql
MAP_CONCAT(map1, map2)
```

## SQLの例

```sql
SELECT MAP_CONCAT(MAP{'a':1}, MAP{'b':2});

┌───────────────┐
│ {"a":1,"b":2} │
└───────────────┘
```
