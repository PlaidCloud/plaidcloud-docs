---
title: GEOHASH_ENCODE (Lakehouse v1)
description: GEOHASH_ENCODE — convierte un par de coordenadas de latitud y longitud en una cadena codificada con Geohash.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geohash-encode.md
---

Convierte un par de coordenadas de latitud y longitud en una cadena codificada con [Geohash](https://en.wikipedia.org/wiki/Geohash).

## Sintaxis de Analyze

```python
func.geohash_encode(lon, lat)
```

## Ejemplos de Analyze

```python
func.geohash_encode(-5.60302734375, 42.593994140625)

┌─────────────────────────────────────────────────────────┐
│ func.geohash_encode((- 5.60302734375), 42.593994140625) │
├─────────────────────────────────────────────────────────┤
│ ezs42d000000                                            │
└─────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
GEOHASH_ENCODE(lon, lat)
```

## Ejemplos de SQL

```sql
SELECT GEOHASH_ENCODE(-5.60302734375, 42.593994140625);

┌────────────────────────────────────────────────────┐
│ geohash_encode((- 5.60302734375), 42.593994140625) │
├────────────────────────────────────────────────────┤
│ ezs42d000000                                       │
└────────────────────────────────────────────────────┘
```
