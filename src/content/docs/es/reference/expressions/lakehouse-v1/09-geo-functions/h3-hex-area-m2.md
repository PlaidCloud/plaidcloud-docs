---
title: H3_HEX_AREA_M2 (Lakehouse v1)
description: H3_HEX_AREA_M2 — devuelve el área media de un hexágono en metros cuadrados para la resolución dada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-hex-area-m2.md
---

Devuelve el área media de un hexágono en metros cuadrados para la resolución dada. Excluye los pentágonos. 

## Sintaxis de Analyze

```python
func.h3_hex_area_m2(res)
```

## Ejemplos de Analyze

```python
func.h3_hex_area_m2(1)

┌────────────────────────┐
│ func.h3_hex_area_m2(1) │
├────────────────────────┤
│      609788441794.1339 │
└────────────────────────┘
```

## Sintaxis de SQL

```sql
H3_HEX_AREA_M2(res)
```

## Ejemplos de SQL

```sql
SELECT H3_HEX_AREA_M2(1);

┌───────────────────┐
│ h3_hex_area_m2(1) │
├───────────────────┤
│ 609788441794.1339 │
└───────────────────┘
```
