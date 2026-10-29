---
title: MAP_CONCAT (Lakehouse v2)
description: MAP_CONCAT — concatène plusieurs maps en un seul map.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-concat.md
---

Concatène plusieurs maps en un seul map.

## Syntaxe Analyze

```python
func.map_concat(map1, map2)
```

## Exemples Analyze

```python
func.map_concat(MAP{'a':1}, MAP{'b':2})

┌───────────────┐
│ {'a':1,'b':2} │
└───────────────┘
```

## Syntaxe SQL

```sql
MAP_CONCAT(map1, map2)
```

## Exemples SQL

```sql
SELECT MAP_CONCAT(MAP{'a':1}, MAP{'b':2});

┌───────────────┐
│ {"a":1,"b":2} │
└───────────────┘
```
