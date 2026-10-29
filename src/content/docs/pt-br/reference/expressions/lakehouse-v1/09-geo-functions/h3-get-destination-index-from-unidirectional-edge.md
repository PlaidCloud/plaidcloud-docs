---
title: H3_GET_DESTINATION_INDEX_FROM_UNIDIRECTIONAL_EDGE (Lakehouse v1)
description: H3_GET_DESTINATION_INDEX_FROM_UNIDIRECTIONAL_EDGE — retorna o índice do hexágono de destino a partir do H3Index da aresta unidirecional.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-destination-index-from-unidirectional-edge.md
---

Retorna o índice do hexágono de destino a partir do H3Index da aresta unidirecional.

## Sintaxe do Analyze

```python
func.h3_get_destination_index_from_unidirectional_edge(h3)
```

## Exemplos do Analyze

```python
func.h3_get_destination_index_from_unidirectional_edge(1248204388774707199)

┌─────────────────────────────────────────────────────────────────────────────┐
│ func.h3_get_destination_index_from_unidirectional_edge(1248204388774707199) │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                          599686043507097599 │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
H3_GET_DESTINATION_INDEX_FROM_UNIDIRECTIONAL_EDGE(h3)
```

## Exemplos de SQL

```sql
SELECT H3_GET_DESTINATION_INDEX_FROM_UNIDIRECTIONAL_EDGE(1248204388774707199);

┌────────────────────────────────────────────────────────────────────────┐
│ h3_get_destination_index_from_unidirectional_edge(1248204388774707199) │
├────────────────────────────────────────────────────────────────────────┤
│                                                     599686043507097599 │
└────────────────────────────────────────────────────────────────────────┘
```
