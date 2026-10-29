---
title: MAP_APPLY (Lakehouse v2)
description: MAP_APPLY — applique une expression lambda à chaque paire clé-valeur d'un map.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-apply.md
---

Applique une expression lambda à chaque paire clé-valeur d'un map.

## Syntaxe Analyze

```python
func.map_apply(get_column(table, 'map_col'), lambda k, v: (k, v*2))
```

## Exemples Analyze

```python
func.map_apply(MAP{'a':1,'b':2}, lambda k,v: (k, v*2))

┌───────────────┐
│ {'a':2,'b':4} │
└───────────────┘
```

## Syntaxe SQL

```sql
MAP_APPLY(<map_col>, lambda k, v: (k, v*2))
```

## Exemples SQL

```sql
SELECT MAP_APPLY((k, v) -> (k, v * 2), MAP{'a':1, 'b':2});

┌───────────────┐
│ {"a":2,"b":4} │
└───────────────┘
```
