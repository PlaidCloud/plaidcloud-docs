---
title: H3_HEX_AREA_KM2 (Lakehouse v1)
description: H3_HEX_AREA_KM2 — zwraca średnią powierzchnię heksagonu w kilometrach kwadratowych dla danej rozdzielczości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-hex-area-km2.md
---

Zwraca średnią powierzchnię heksagonu w kilometrach kwadratowych dla danej rozdzielczości. Nie obejmuje pentagonów.

## Składnia Analyze

```python
func.h3_area_km2(res)
```

## Przykłady Analyze

```python
func.h3_area_km2(1)

┌─────────────────────────┐
│ func.h3_hex_area_km2(1) │
├─────────────────────────┤
│       609788.4417941332 │
└─────────────────────────┘
```

## Składnia SQL

```sql
H3_HEX_AREA_KM2(res)
```

## Przykłady SQL

```sql
SELECT H3_HEX_AREA_KM2(1);

┌────────────────────┐
│ h3_hex_area_km2(1) │
├────────────────────┤
│  609788.4417941332 │
└────────────────────┘
```
