---
title: MAP_CONCAT (Lakehouse v2)
description: MAP_CONCAT – verkettet mehrere Maps zu einer einzelnen Map.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-concat.md
---

Verkettet mehrere Maps zu einer einzelnen Map.

## Analyze-Syntax

```python
func.map_concat(map1, map2)
```

## Analyze-Beispiele

```python
func.map_concat(MAP{'a':1}, MAP{'b':2})

┌───────────────┐
│ {'a':1,'b':2} │
└───────────────┘
```

## SQL-Syntax

```sql
MAP_CONCAT(map1, map2)
```

## SQL-Beispiele

```sql
SELECT MAP_CONCAT(MAP{'a':1}, MAP{'b':2});

┌───────────────┐
│ {"a":1,"b":2} │
└───────────────┘
```
