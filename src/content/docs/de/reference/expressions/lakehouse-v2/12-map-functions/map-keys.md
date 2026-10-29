---
title: MAP_KEYS (Lakehouse v2)
description: MAP_KEYS – gibt alle Schlüssel einer Map als Array zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-keys.md
---

Gibt alle Schlüssel einer Map als Array zurück.

## Analyze-Syntax

```python
func.map_keys(get_column(table, 'map_col'))
```

## Analyze-Beispiele

```python
func.map_keys(MAP{'a':1,'b':2})

┌───────────┐
│ ['a','b'] │
└───────────┘
```

## SQL-Syntax

```sql
MAP_KEYS(<map_col>)
```

## SQL-Beispiele

```sql
SELECT MAP_KEYS(MAP{'a':1, 'b':2});

┌───────────┐
│ ["a","b"] │
└───────────┘
```
