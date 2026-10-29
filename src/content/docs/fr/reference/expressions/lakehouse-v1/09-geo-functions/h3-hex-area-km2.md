---
title: H3_HEX_AREA_KM2 (Lakehouse v1)
description: H3_HEX_AREA_KM2 — renvoie la superficie moyenne d'un hexagone, en kilomètres carrés, à la résolution donnée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-hex-area-km2.md
---

Renvoie la superficie moyenne d'un hexagone, en kilomètres carrés, à la résolution donnée. Les pentagones sont exclus.

## Syntaxe Analyze

```python
func.h3_area_km2(res)
```

## Exemples Analyze

```python
func.h3_area_km2(1)

┌─────────────────────────┐
│ func.h3_hex_area_km2(1) │
├─────────────────────────┤
│       609788.4417941332 │
└─────────────────────────┘
```

## Syntaxe SQL

```sql
H3_HEX_AREA_KM2(res)
```

## Exemples SQL

```sql
SELECT H3_HEX_AREA_KM2(1);

┌────────────────────┐
│ h3_hex_area_km2(1) │
├────────────────────┤
│  609788.4417941332 │
└────────────────────┘
```
