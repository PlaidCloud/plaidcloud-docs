---
title: TRANSFORM_VALUES (Lakehouse v2)
description: TRANSFORM_VALUES – wendet einen Lambda-Ausdruck an, um die Werte einer Map zu transformieren.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/transform-values.md
---

Wendet einen Lambda-Ausdruck an, um die Werte einer Map zu transformieren.

## Analyze-Syntax

```python
func.transform_values(get_column(table, 'map_col'), lambda k, v: v * 10)
```

## Analyze-Beispiele

```python
func.transform_values(MAP{'a':1,'b':2}, lambda k,v: v*10)

┌─────────────────┐
│ {'a':10,'b':20} │
└─────────────────┘
```

## SQL-Syntax

```sql
TRANSFORM_VALUES(<map_col>, lambda k, v: v * 10)
```

## SQL-Beispiele

```sql
SELECT TRANSFORM_VALUES((k, v) -> v * 10, MAP{'a':1, 'b':2});

┌─────────────────┐
│ {"a":10,"b":20} │
└─────────────────┘
```
