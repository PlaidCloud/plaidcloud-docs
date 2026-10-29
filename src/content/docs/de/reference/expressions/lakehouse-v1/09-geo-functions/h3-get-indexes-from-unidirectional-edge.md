---
title: H3_GET_INDEXES_FROM_UNIDIRECTIONAL_EDGE (Lakehouse v1)
description: H3_GET_INDEXES_FROM_UNIDIRECTIONAL_EDGE — gibt die Ursprungs- und Zielhexagon-Indizes zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-indexes-from-unidirectional-edge.md
---

Gibt die Ursprungs- und Zielhexagon-Indizes aus dem angegebenen H3Index der gerichteten Kante zurück.

## Analyze-Syntax

```python
func.h3_get_indexes_from_unidirectional_edge(h3)
```

## Analyze-Beispiele

```python
func.h3_get_indexes_from_unidirectional_edge(1248204388774707199)

┌────────────────────────────────────────────────────────────────────┐
│ func.h3_get_indexes_from_unidirectional_edge(1248204388774707199)  │
├────────────────────────────────────────────────────────────────────┤
│ (599686042433355775,599686043507097599)                            │
└────────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
H3_GET_INDEXES_FROM_UNIDIRECTIONAL_EDGE(h3)
```

## SQL-Beispiele

```sql
SELECT H3_GET_INDEXES_FROM_UNIDIRECTIONAL_EDGE(1248204388774707199);

┌──────────────────────────────────────────────────────────────┐
│ h3_get_indexes_from_unidirectional_edge(1248204388774707199) │
├──────────────────────────────────────────────────────────────┤
│ (599686042433355775,599686043507097599)                      │
└──────────────────────────────────────────────────────────────┘
```
