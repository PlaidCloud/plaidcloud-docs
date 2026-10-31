---
title: MAP_FROM_ARRAYS (Lakehouse v2)
description: MAP_FROM_ARRAYS — crée un map à partir d'un tableau de clés et d'un tableau de valeurs.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-from-arrays.md
---

Crée un map à partir d'un tableau de clés et d'un tableau de valeurs.

## Syntaxe Analyze

```python
func.map_from_arrays(['a','b'], [1, 2])
```

## Exemples Analyze

```python
func.map_from_arrays(['a', 'b', 'c'], [1, 2, 3])

┌─────────────────────┐
│ {'a':1,'b':2,'c':3} │
└─────────────────────┘
```

## Syntaxe SQL

```sql
MAP_FROM_ARRAYS(['a','b'], [1, 2])
```

## Exemples SQL

```sql
SELECT MAP_FROM_ARRAYS(['a', 'b', 'c'], [1, 2, 3]);

┌─────────────────────┐
│ {"a":1,"b":2,"c":3} │
└─────────────────────┘
```
