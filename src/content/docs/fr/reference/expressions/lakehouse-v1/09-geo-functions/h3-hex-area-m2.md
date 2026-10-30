---
title: H3_HEX_AREA_M2 (Lakehouse v1)
description: H3_HEX_AREA_M2 — renvoie la superficie moyenne d'un hexagone, en mètres carrés, à la résolution donnée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-hex-area-m2.md
---

Renvoie la superficie moyenne d'un hexagone, en mètres carrés, à la résolution donnée. Les pentagones sont exclus.

## Syntaxe Analyze

```python
func.h3_hex_area_m2(res)
```

## Exemples Analyze

```python
func.h3_hex_area_m2(1)

┌────────────────────────┐
│ func.h3_hex_area_m2(1) │
├────────────────────────┤
│      609788441794.1339 │
└────────────────────────┘
```

## Syntaxe SQL

```sql
H3_HEX_AREA_M2(res)
```

## Exemples SQL

```sql
SELECT H3_HEX_AREA_M2(1);

┌───────────────────┐
│ h3_hex_area_m2(1) │
├───────────────────┤
│ 609788441794.1339 │
└───────────────────┘
```
