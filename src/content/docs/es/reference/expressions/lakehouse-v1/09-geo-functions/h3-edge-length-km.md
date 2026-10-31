---
title: H3_EDGE_LENGTH_KM (Lakehouse v1)
description: H3_EDGE_LENGTH_KM — devuelve la longitud media de la arista de un hexágono en kilómetros para la resolución dada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-edge-length-km.md
---

Devuelve la longitud media de la arista de un hexágono en kilómetros para la resolución dada. Excluye los pentágonos.

## Sintaxis de Analyze

```python
func.h3_edge_length_km(res)
```

## Ejemplos de Analyze

```python
func.h3_edge_length_km(1)

┌───────────────────────────┐
│ func.h3_edge_length_km(1) │
├───────────────────────────┤
│         483.0568390711111 │
└───────────────────────────┘
```

## Sintaxis de SQL

```sql
H3_EDGE_LENGTH_KM(res)
```

## Ejemplos de SQL

```sql
SELECT H3_EDGE_LENGTH_KM(1);

┌──────────────────────┐
│ h3_edge_length_km(1) │
├──────────────────────┤
│    483.0568390711111 │
└──────────────────────┘
```
