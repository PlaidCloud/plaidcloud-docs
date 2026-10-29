---
title: GEO_TO_H3 (Lakehouse v1)
description: GEO_TO_H3 — zwraca indeks H3 komórki heksagonalnej, w której znajduje się dana lokalizacja.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geo-to-h3.md
---

Zwraca indeks [H3](https://eng.uber.com/h3/) komórki heksagonalnej, w której znajduje się dana lokalizacja. Zwrócenie wartości 0 oznacza wystąpienie błędu.

## Składnia Analyze

```python
func.geo_to_h3(lon, lat, res)
```

## Przykłady Analyze

```python
func.geo_to_h3(37.79506683, 55.71290588, 15)

┌──────────────────────────────────────────────┐
│ func.geo_to_h3(37.79506683, 55.71290588, 15) │
├──────────────────────────────────────────────┤
│                           644325524701193974 │
└──────────────────────────────────────────────┘
```

## Składnia SQL

```sql
GEO_TO_H3(lon, lat, res)
```

## Przykłady SQL

```sql
SELECT GEO_TO_H3(37.79506683, 55.71290588, 15);

┌─────────────────────────────────────────┐
│ geo_to_h3(37.79506683, 55.71290588, 15) │
├─────────────────────────────────────────┤
│                      644325524701193974 │
└─────────────────────────────────────────┘
```
