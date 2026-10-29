---
title: H3_GET_UNIDIRECTIONAL_EDGES_FROM_HEXAGON (Lakehouse v1)
description: H3_GET_UNIDIRECTIONAL_EDGES_FROM_HEXAGON — retorna todas as arestas unidirecionais a partir do H3Index informado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-unidirectional-edges-from-hexagon.md
---

Retorna todas as arestas unidirecionais a partir do H3Index informado.

## Sintaxe do Analyze

```python
func.h3_get_unidirectional_edges_from_hexagon(h3)
```

## Exemplos do Analyze

```python
func.h3_get_unidirectional_edges_from_hexagon(644325524701193754)

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              func.h3_get_unidirectional_edges_from_hexagon(644325524701193754)                            │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [1292843871042545178,1364901465080473114,1436959059118401050,1509016653156328986,1581074247194256922,1653131841232184858] │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
H3_GET_UNIDIRECTIONAL_EDGES_FROM_HEXAGON(h3)
```

## Exemplos de SQL

```sql
SELECT H3_GET_UNIDIRECTIONAL_EDGES_FROM_HEXAGON(644325524701193754);

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                h3_get_unidirectional_edges_from_hexagon(644325524701193754)                               │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [1292843871042545178,1364901465080473114,1436959059118401050,1509016653156328986,1581074247194256922,1653131841232184858] │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
