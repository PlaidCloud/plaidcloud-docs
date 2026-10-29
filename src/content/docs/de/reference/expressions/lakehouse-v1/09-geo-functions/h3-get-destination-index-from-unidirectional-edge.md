---
title: H3_GET_DESTINATION_INDEX_FROM_UNIDIRECTIONAL_EDGE (Lakehouse v1)
description: H3_GET_DESTINATION_INDEX_FROM_UNIDIRECTIONAL_EDGE — gibt den Zielhexagon-Index aus dem H3Index der gerichteten Kante zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-destination-index-from-unidirectional-edge.md
---

Gibt den Zielhexagon-Index aus dem H3Index der gerichteten Kante zurück.

## Analyze-Syntax

```python
func.h3_get_destination_index_from_unidirectional_edge(h3)
```

## Analyze-Beispiele

```python
func.h3_get_destination_index_from_unidirectional_edge(1248204388774707199)

┌─────────────────────────────────────────────────────────────────────────────┐
│ func.h3_get_destination_index_from_unidirectional_edge(1248204388774707199) │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                          599686043507097599 │
└─────────────────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
H3_GET_DESTINATION_INDEX_FROM_UNIDIRECTIONAL_EDGE(h3)
```

## SQL-Beispiele

```sql
SELECT H3_GET_DESTINATION_INDEX_FROM_UNIDIRECTIONAL_EDGE(1248204388774707199);

┌────────────────────────────────────────────────────────────────────────┐
│ h3_get_destination_index_from_unidirectional_edge(1248204388774707199) │
├────────────────────────────────────────────────────────────────────────┤
│                                                     599686043507097599 │
└────────────────────────────────────────────────────────────────────────┘
```
