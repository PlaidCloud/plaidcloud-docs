---
title: GEOHASH_DECODE (Lakehouse v1)
description: GEOHASH_DECODE — convertit une chaîne encodée en Geohash en coordonnées de latitude et de longitude.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geohash-decode.md
---

Convertit une chaîne encodée en [Geohash](https://en.wikipedia.org/wiki/Geohash) en coordonnées de latitude et de longitude.

## Syntaxe Analyze

```python
func.geohash_decode('<geohashed-string\>')
```

## Exemples Analyze

```python
func.geohash_decode('ezs42')

┌─────────────────────────────────┐
│  func.geohash_decode('ezs42')   │
├─────────────────────────────────┤
│ (-5.60302734375,42.60498046875) │
└─────────────────────────────────┘
```

## Syntaxe SQL

```sql
GEOHASH_DECODE('<geohashed-string\>')
```

## Exemples SQL

```sql
SELECT GEOHASH_DECODE('ezs42');

┌─────────────────────────────────┐
│     geohash_decode('ezs42')     │
├─────────────────────────────────┤
│ (-5.60302734375,42.60498046875) │
└─────────────────────────────────┘
```
