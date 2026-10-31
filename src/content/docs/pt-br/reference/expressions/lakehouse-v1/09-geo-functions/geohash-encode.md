---
title: GEOHASH_ENCODE (Lakehouse v1)
description: GEOHASH_ENCODE — converte um par de coordenadas de latitude e longitude em uma string codificada em Geohash.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geohash-encode.md
---

Converte um par de coordenadas de latitude e longitude em uma string codificada em [Geohash](https://en.wikipedia.org/wiki/Geohash).

## Sintaxe do Analyze

```python
func.geohash_encode(lon, lat)
```

## Exemplos do Analyze

```python
func.geohash_encode(-5.60302734375, 42.593994140625)

┌─────────────────────────────────────────────────────────┐
│ func.geohash_encode((- 5.60302734375), 42.593994140625) │
├─────────────────────────────────────────────────────────┤
│ ezs42d000000                                            │
└─────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
GEOHASH_ENCODE(lon, lat)
```

## Exemplos de SQL

```sql
SELECT GEOHASH_ENCODE(-5.60302734375, 42.593994140625);

┌────────────────────────────────────────────────────┐
│ geohash_encode((- 5.60302734375), 42.593994140625) │
├────────────────────────────────────────────────────┤
│ ezs42d000000                                       │
└────────────────────────────────────────────────────┘
```
