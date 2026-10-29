---
title: GEO_TO_H3 (Lakehouse v1)
description: GEO_TO_H3 — devuelve el índice H3 de la celda hexagonal donde se encuentra la ubicación dada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geo-to-h3.md
---

Devuelve el índice [H3](https://eng.uber.com/h3/) de la celda hexagonal donde se encuentra la ubicación dada. Un resultado de 0 indica que se produjo un error.

## Sintaxis de Analyze

```python
func.geo_to_h3(lon, lat, res)
```

## Ejemplos de Analyze

```python
func.geo_to_h3(37.79506683, 55.71290588, 15)

┌──────────────────────────────────────────────┐
│ func.geo_to_h3(37.79506683, 55.71290588, 15) │
├──────────────────────────────────────────────┤
│                           644325524701193974 │
└──────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
GEO_TO_H3(lon, lat, res)
```

## Ejemplos de SQL

```sql
SELECT GEO_TO_H3(37.79506683, 55.71290588, 15);

┌─────────────────────────────────────────┐
│ geo_to_h3(37.79506683, 55.71290588, 15) │
├─────────────────────────────────────────┤
│                      644325524701193974 │
└─────────────────────────────────────────┘
```
