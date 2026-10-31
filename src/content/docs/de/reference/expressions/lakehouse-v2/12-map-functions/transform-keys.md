---
title: TRANSFORM_KEYS (Lakehouse v2)
description: TRANSFORM_KEYS – wendet einen Lambda-Ausdruck an, um die Schlüssel einer Map zu transformieren.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/transform-keys.md
---

Wendet einen Lambda-Ausdruck an, um die Schlüssel einer Map zu transformieren.

## Analyze-Syntax

```python
func.transform_keys(get_column(table, 'map_col'), lambda k, v: upper(k))
```

## Analyze-Beispiele

```python
func.transform_keys(MAP{'a':1,'b':2}, lambda k,v: upper(k))

┌───────────────┐
│ {'A':1,'B':2} │
└───────────────┘
```

## SQL-Syntax

```sql
TRANSFORM_KEYS(<map_col>, lambda k, v: upper(k))
```

## SQL-Beispiele

```sql
SELECT TRANSFORM_KEYS((k, v) -> UPPER(k), MAP{'a':1, 'b':2});

┌───────────────┐
│ {"A":1,"B":2} │
└───────────────┘
```
