---
title: H3_GET_ORIGIN_INDEX_FROM_UNIDIRECTIONAL_EDGE (Lakehouse v1)
description: H3_GET_ORIGIN_INDEX_FROM_UNIDIRECTIONAL_EDGE — devuelve el índice del hexágono de origen a partir del H3Index de la arista unidireccional.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-origin-index-from-unidirectional-edge.md
---

Devuelve el índice del hexágono de origen a partir del H3Index de la arista unidireccional.

## Sintaxis de Analyze

```python
func.h3_get_origin_index_from_unidirectional_edge(h3)
```

## Ejemplos de Analyze

```python
func.h3_get_origin_index_from_unidirectional_edge(1248204388774707199)

┌────────────────────────────────────────────────────────────────────────┐
│ func.h3_get_origin_index_from_unidirectional_edge(1248204388774707199) │
├────────────────────────────────────────────────────────────────────────┤
│                                                     599686042433355775 │
└────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
H3_GET_ORIGIN_INDEX_FROM_UNIDIRECTIONAL_EDGE(h3)
```

## Ejemplos de SQL

```sql
SELECT H3_GET_ORIGIN_INDEX_FROM_UNIDIRECTIONAL_EDGE(1248204388774707199);

┌───────────────────────────────────────────────────────────────────┐
│ h3_get_origin_index_from_unidirectional_edge(1248204388774707199) │
├───────────────────────────────────────────────────────────────────┤
│                                                599686042433355775 │
└───────────────────────────────────────────────────────────────────┘
```
