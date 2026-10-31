---
title: GEOHASH_DECODE (Lakehouse v1)
description: GEOHASH_DECODE — konwertuje ciąg zakodowany w Geohash na współrzędne szerokości i długości geograficznej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geohash-decode.md
---

Konwertuje ciąg zakodowany w [Geohash](https://en.wikipedia.org/wiki/Geohash) na współrzędne szerokości i długości geograficznej.

## Składnia Analyze

```python
func.geohash_decode('<geohashed-string\>')
```

## Przykłady Analyze

```python
func.geohash_decode('ezs42')

┌─────────────────────────────────┐
│  func.geohash_decode('ezs42')   │
├─────────────────────────────────┤
│ (-5.60302734375,42.60498046875) │
└─────────────────────────────────┘
```

## Składnia SQL

```sql
GEOHASH_DECODE('<geohashed-string\>')
```

## Przykłady SQL

```sql
SELECT GEOHASH_DECODE('ezs42');

┌─────────────────────────────────┐
│     geohash_decode('ezs42')     │
├─────────────────────────────────┤
│ (-5.60302734375,42.60498046875) │
└─────────────────────────────────┘
```
