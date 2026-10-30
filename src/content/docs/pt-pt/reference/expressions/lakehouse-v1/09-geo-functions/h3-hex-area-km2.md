---
title: H3_HEX_AREA_KM2 (Lakehouse v1)
description: H3_HEX_AREA_KM2 — devolve a área média do hexágono em quilómetros quadrados na resolução indicada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-hex-area-km2.md
---

Devolve a área média do hexágono em quilómetros quadrados na resolução indicada. Exclui pentágonos.

## Sintaxe do Analyze

```python
func.h3_area_km2(res)
```

## Exemplos do Analyze

```python
func.h3_area_km2(1)

┌─────────────────────────┐
│ func.h3_hex_area_km2(1) │
├─────────────────────────┤
│       609788.4417941332 │
└─────────────────────────┘
```

## Sintaxe SQL

```sql
H3_HEX_AREA_KM2(res)
```

## Exemplos de SQL

```sql
SELECT H3_HEX_AREA_KM2(1);

┌────────────────────┐
│ h3_hex_area_km2(1) │
├────────────────────┤
│  609788.4417941332 │
└────────────────────┘
```
