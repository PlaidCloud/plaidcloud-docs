---
title: GEOHASH_DECODE (Lakehouse v1)
description: GEOHASH_DECODE — converte uma string codificada em Geohash em coordenadas de latitude/longitude.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geohash-decode.md
---

Converte uma string codificada em [Geohash](https://en.wikipedia.org/wiki/Geohash) em coordenadas de latitude/longitude.

## Sintaxe do Analyze

```python
func.geohash_decode('<geohashed-string\>')
```

## Exemplos do Analyze

```python
func.geohash_decode('ezs42')

┌─────────────────────────────────┐
│  func.geohash_decode('ezs42')   │
├─────────────────────────────────┤
│ (-5.60302734375,42.60498046875) │
└─────────────────────────────────┘
```

## Sintaxe SQL

```sql
GEOHASH_DECODE('<geohashed-string\>')
```

## Exemplos de SQL

```sql
SELECT GEOHASH_DECODE('ezs42');

┌─────────────────────────────────┐
│     geohash_decode('ezs42')     │
├─────────────────────────────────┤
│ (-5.60302734375,42.60498046875) │
└─────────────────────────────────┘
```
