---
title: H3_HEX_AREA_KM2 (Lakehouse v1)
description: H3_HEX_AREA_KM2 — devuelve el área media de un hexágono en kilómetros cuadrados para la resolución dada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-hex-area-km2.md
---

Devuelve el área media de un hexágono en kilómetros cuadrados para la resolución dada. Excluye los pentágonos.

## Sintaxis de Analyze

```python
func.h3_area_km2(res)
```

## Ejemplos de Analyze

```python
func.h3_area_km2(1)

┌─────────────────────────┐
│ func.h3_hex_area_km2(1) │
├─────────────────────────┤
│       609788.4417941332 │
└─────────────────────────┘
```

## Sintaxis de SQL

```sql
H3_HEX_AREA_KM2(res)
```

## Ejemplos de SQL

```sql
SELECT H3_HEX_AREA_KM2(1);

┌────────────────────┐
│ h3_hex_area_km2(1) │
├────────────────────┤
│  609788.4417941332 │
└────────────────────┘
```
