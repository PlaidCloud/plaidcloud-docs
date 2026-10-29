---
title: H3_HEX_AREA_KM2 (Lakehouse v1)
description: H3_HEX_AREA_KM2 — gibt die durchschnittliche Hexagonfläche in Quadratkilometern bei der angegebenen Auflösung zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-hex-area-km2.md
---

Gibt die durchschnittliche Hexagonfläche in Quadratkilometern bei der angegebenen Auflösung zurück. Fünfecke sind ausgenommen.

## Analyze-Syntax

```python
func.h3_area_km2(res)
```

## Analyze-Beispiele

```python
func.h3_area_km2(1)

┌─────────────────────────┐
│ func.h3_hex_area_km2(1) │
├─────────────────────────┤
│       609788.4417941332 │
└─────────────────────────┘
```

## SQL-Syntax

```sql
H3_HEX_AREA_KM2(res)
```

## SQL-Beispiele

```sql
SELECT H3_HEX_AREA_KM2(1);

┌────────────────────┐
│ h3_hex_area_km2(1) │
├────────────────────┤
│  609788.4417941332 │
└────────────────────┘
```
