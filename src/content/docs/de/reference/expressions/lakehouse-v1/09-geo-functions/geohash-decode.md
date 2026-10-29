---
title: GEOHASH_DECODE (Lakehouse v1)
description: GEOHASH_DECODE — wandelt eine Geohash-codierte Zeichenfolge in Breiten- und Längengradkoordinaten um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geohash-decode.md
---

Wandelt eine [Geohash](https://en.wikipedia.org/wiki/Geohash)-codierte Zeichenfolge in Breiten- und Längengradkoordinaten um.

## Analyze-Syntax

```python
func.geohash_decode('<geohashed-string\>')
```

## Analyze-Beispiele

```python
func.geohash_decode('ezs42')

┌─────────────────────────────────┐
│  func.geohash_decode('ezs42')   │
├─────────────────────────────────┤
│ (-5.60302734375,42.60498046875) │
└─────────────────────────────────┘
```

## SQL-Syntax

```sql
GEOHASH_DECODE('<geohashed-string\>')
```

## SQL-Beispiele

```sql
SELECT GEOHASH_DECODE('ezs42');

┌─────────────────────────────────┐
│     geohash_decode('ezs42')     │
├─────────────────────────────────┤
│ (-5.60302734375,42.60498046875) │
└─────────────────────────────────┘
```
