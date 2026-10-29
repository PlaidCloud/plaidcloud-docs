---
title: TRANSFORM_KEYS (Lakehouse v2)
description: TRANSFORM_KEYS — applique une expression lambda pour transformer les clés d'un map.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/transform-keys.md
---

Applique une expression lambda pour transformer les clés d'un map.

## Syntaxe Analyze

```python
func.transform_keys(get_column(table, 'map_col'), lambda k, v: upper(k))
```

## Exemples Analyze

```python
func.transform_keys(MAP{'a':1,'b':2}, lambda k,v: upper(k))

┌───────────────┐
│ {'A':1,'B':2} │
└───────────────┘
```

## Syntaxe SQL

```sql
TRANSFORM_KEYS(<map_col>, lambda k, v: upper(k))
```

## Exemples SQL

```sql
SELECT TRANSFORM_KEYS((k, v) -> UPPER(k), MAP{'a':1, 'b':2});

┌───────────────┐
│ {"A":1,"B":2} │
└───────────────┘
```
