---
title: GEOHASH_DECODE (Lakehouse v1)
description: GEOHASH_DECODE — convierte una cadena codificada con Geohash en coordenadas de latitud y longitud.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geohash-decode.md
---

Convierte una cadena codificada con [Geohash](https://en.wikipedia.org/wiki/Geohash) en coordenadas de latitud y longitud.

## Sintaxis de Analyze

```python
func.geohash_decode('<geohashed-string\>')
```

## Ejemplos de Analyze

```python
func.geohash_decode('ezs42')

┌─────────────────────────────────┐
│  func.geohash_decode('ezs42')   │
├─────────────────────────────────┤
│ (-5.60302734375,42.60498046875) │
└─────────────────────────────────┘
```

## Sintaxis de SQL

```sql
GEOHASH_DECODE('<geohashed-string\>')
```

## Ejemplos de SQL

```sql
SELECT GEOHASH_DECODE('ezs42');

┌─────────────────────────────────┐
│     geohash_decode('ezs42')     │
├─────────────────────────────────┤
│ (-5.60302734375,42.60498046875) │
└─────────────────────────────────┘
```
