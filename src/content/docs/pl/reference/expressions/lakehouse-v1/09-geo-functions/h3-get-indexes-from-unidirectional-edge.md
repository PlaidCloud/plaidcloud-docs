---
title: H3_GET_INDEXES_FROM_UNIDIRECTIONAL_EDGE (Lakehouse v1)
description: H3_GET_INDEXES_FROM_UNIDIRECTIONAL_EDGE — zwraca indeksy heksagonu początkowego i docelowego.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-indexes-from-unidirectional-edge.md
---

Zwraca indeksy heksagonu początkowego i docelowego z podanej jednokierunkowej krawędzi H3Index.

## Składnia Analyze

```python
func.h3_get_indexes_from_unidirectional_edge(h3)
```

## Przykłady Analyze

```python
func.h3_get_indexes_from_unidirectional_edge(1248204388774707199)

┌────────────────────────────────────────────────────────────────────┐
│ func.h3_get_indexes_from_unidirectional_edge(1248204388774707199)  │
├────────────────────────────────────────────────────────────────────┤
│ (599686042433355775,599686043507097599)                            │
└────────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
H3_GET_INDEXES_FROM_UNIDIRECTIONAL_EDGE(h3)
```

## Przykłady SQL

```sql
SELECT H3_GET_INDEXES_FROM_UNIDIRECTIONAL_EDGE(1248204388774707199);

┌──────────────────────────────────────────────────────────────┐
│ h3_get_indexes_from_unidirectional_edge(1248204388774707199) │
├──────────────────────────────────────────────────────────────┤
│ (599686042433355775,599686043507097599)                      │
└──────────────────────────────────────────────────────────────┘
```
