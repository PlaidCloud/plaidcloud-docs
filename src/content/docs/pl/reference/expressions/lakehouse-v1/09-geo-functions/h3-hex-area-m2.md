---
title: H3_HEX_AREA_M2 (Lakehouse v1)
description: H3_HEX_AREA_M2 — zwraca średnią powierzchnię heksagonu w metrach kwadratowych dla danej rozdzielczości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-hex-area-m2.md
---

Zwraca średnią powierzchnię heksagonu w metrach kwadratowych dla danej rozdzielczości. Nie obejmuje pentagonów. 

## Składnia Analyze

```python
func.h3_hex_area_m2(res)
```

## Przykłady Analyze

```python
func.h3_hex_area_m2(1)

┌────────────────────────┐
│ func.h3_hex_area_m2(1) │
├────────────────────────┤
│      609788441794.1339 │
└────────────────────────┘
```

## Składnia SQL

```sql
H3_HEX_AREA_M2(res)
```

## Przykłady SQL

```sql
SELECT H3_HEX_AREA_M2(1);

┌───────────────────┐
│ h3_hex_area_m2(1) │
├───────────────────┤
│ 609788441794.1339 │
└───────────────────┘
```
