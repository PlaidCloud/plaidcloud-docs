---
title: H3_HEX_AREA_M2 (Lakehouse v1)
description: H3_HEX_AREA_M2 — gibt die durchschnittliche Hexagonfläche in Quadratmetern bei der angegebenen Auflösung zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-hex-area-m2.md
---

Gibt die durchschnittliche Hexagonfläche in Quadratmetern bei der angegebenen Auflösung zurück. Fünfecke sind ausgenommen.

## Analyze-Syntax

```python
func.h3_hex_area_m2(res)
```

## Analyze-Beispiele

```python
func.h3_hex_area_m2(1)

┌────────────────────────┐
│ func.h3_hex_area_m2(1) │
├────────────────────────┤
│      609788441794.1339 │
└────────────────────────┘
```

## SQL-Syntax

```sql
H3_HEX_AREA_M2(res)
```

## SQL-Beispiele

```sql
SELECT H3_HEX_AREA_M2(1);

┌───────────────────┐
│ h3_hex_area_m2(1) │
├───────────────────┤
│ 609788441794.1339 │
└───────────────────┘
```
