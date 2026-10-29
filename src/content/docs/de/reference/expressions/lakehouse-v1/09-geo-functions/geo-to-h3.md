---
title: GEO_TO_H3 (Lakehouse v1)
description: GEO_TO_H3 — gibt den H3-Index der Hexagonzelle zurück, in der sich der angegebene Standort befindet.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geo-to-h3.md
---

Gibt den [H3](https://eng.uber.com/h3/)-Index der Hexagonzelle zurück, in der sich der angegebene Standort befindet. Der Rückgabewert 0 bedeutet, dass ein Fehler aufgetreten ist.

## Analyze-Syntax

```python
func.geo_to_h3(lon, lat, res)
```

## Analyze-Beispiele

```python
func.geo_to_h3(37.79506683, 55.71290588, 15)

┌──────────────────────────────────────────────┐
│ func.geo_to_h3(37.79506683, 55.71290588, 15) │
├──────────────────────────────────────────────┤
│                           644325524701193974 │
└──────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
GEO_TO_H3(lon, lat, res)
```

## SQL-Beispiele

```sql
SELECT GEO_TO_H3(37.79506683, 55.71290588, 15);

┌─────────────────────────────────────────┐
│ geo_to_h3(37.79506683, 55.71290588, 15) │
├─────────────────────────────────────────┤
│                      644325524701193974 │
└─────────────────────────────────────────┘
```
