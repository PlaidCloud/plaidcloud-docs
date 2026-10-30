---
title: H3_GET_INDEXES_FROM_UNIDIRECTIONAL_EDGE (Lakehouse v1)
description: H3_GET_INDEXES_FROM_UNIDIRECTIONAL_EDGE — devuelve los índices de los hexágonos de origen y de destino.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-indexes-from-unidirectional-edge.md
---

Devuelve los índices de los hexágonos de origen y de destino a partir del H3Index de la arista unidireccional dada.

## Sintaxis de Analyze

```python
func.h3_get_indexes_from_unidirectional_edge(h3)
```

## Ejemplos de Analyze

```python
func.h3_get_indexes_from_unidirectional_edge(1248204388774707199)

┌────────────────────────────────────────────────────────────────────┐
│ func.h3_get_indexes_from_unidirectional_edge(1248204388774707199)  │
├────────────────────────────────────────────────────────────────────┤
│ (599686042433355775,599686043507097599)                            │
└────────────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
H3_GET_INDEXES_FROM_UNIDIRECTIONAL_EDGE(h3)
```

## Ejemplos de SQL

```sql
SELECT H3_GET_INDEXES_FROM_UNIDIRECTIONAL_EDGE(1248204388774707199);

┌──────────────────────────────────────────────────────────────┐
│ h3_get_indexes_from_unidirectional_edge(1248204388774707199) │
├──────────────────────────────────────────────────────────────┤
│ (599686042433355775,599686043507097599)                      │
└──────────────────────────────────────────────────────────────┘
```
