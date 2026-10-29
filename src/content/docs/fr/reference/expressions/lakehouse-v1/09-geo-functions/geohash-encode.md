---
title: GEOHASH_ENCODE (Lakehouse v1)
description: GEOHASH_ENCODE — convertit une paire de coordonnées de latitude et de longitude en chaîne encodée en Geohash.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geohash-encode.md
---

Convertit une paire de coordonnées de latitude et de longitude en chaîne encodée en [Geohash](https://en.wikipedia.org/wiki/Geohash).

## Syntaxe Analyze

```python
func.geohash_encode(lon, lat)
```

## Exemples Analyze

```python
func.geohash_encode(-5.60302734375, 42.593994140625)

┌─────────────────────────────────────────────────────────┐
│ func.geohash_encode((- 5.60302734375), 42.593994140625) │
├─────────────────────────────────────────────────────────┤
│ ezs42d000000                                            │
└─────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
GEOHASH_ENCODE(lon, lat)
```

## Exemples SQL

```sql
SELECT GEOHASH_ENCODE(-5.60302734375, 42.593994140625);

┌────────────────────────────────────────────────────┐
│ geohash_encode((- 5.60302734375), 42.593994140625) │
├────────────────────────────────────────────────────┤
│ ezs42d000000                                       │
└────────────────────────────────────────────────────┘
```
