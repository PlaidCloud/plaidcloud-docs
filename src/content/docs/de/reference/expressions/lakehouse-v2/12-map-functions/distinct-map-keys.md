---
title: DISTINCT_MAP_KEYS (Lakehouse v2)
description: DISTINCT_MAP_KEYS – gibt die eindeutigen Schlüssel einer Map zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/distinct-map-keys.md
---

Gibt die eindeutigen Schlüssel einer Map zurück.

## Analyze-Syntax

```python
func.distinct_map_keys(get_column(table, 'map_col'))
```

## Analyze-Beispiele

```python
func.distinct_map_keys(get_column(table, 'tags'))

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## SQL-Syntax

```sql
DISTINCT_MAP_KEYS(<map_col>)
```

## SQL-Beispiele

```sql
SELECT DISTINCT_MAP_KEYS(MAP{'a':1, 'b':2, 'c':3});

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
