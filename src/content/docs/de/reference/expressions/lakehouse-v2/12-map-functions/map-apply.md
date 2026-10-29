---
title: MAP_APPLY (Lakehouse v2)
description: MAP_APPLY – wendet einen Lambda-Ausdruck auf jedes Schlüssel-Wert-Paar in einer Map an.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-apply.md
---

Wendet einen Lambda-Ausdruck auf jedes Schlüssel-Wert-Paar in einer Map an.

## Analyze-Syntax

```python
func.map_apply(get_column(table, 'map_col'), lambda k, v: (k, v*2))
```

## Analyze-Beispiele

```python
func.map_apply(MAP{'a':1,'b':2}, lambda k,v: (k, v*2))

┌───────────────┐
│ {'a':2,'b':4} │
└───────────────┘
```

## SQL-Syntax

```sql
MAP_APPLY(<map_col>, lambda k, v: (k, v*2))
```

## SQL-Beispiele

```sql
SELECT MAP_APPLY((k, v) -> (k, v * 2), MAP{'a':1, 'b':2});

┌───────────────┐
│ {"a":2,"b":4} │
└───────────────┘
```
