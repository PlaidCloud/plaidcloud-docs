---
title: GEOHASH_ENCODE (Lakehouse v1)
description: GEOHASH_ENCODE — konwertuje parę współrzędnych szerokości i długości geograficznej na ciąg zakodowany w Geohash.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geohash-encode.md
---

Konwertuje parę współrzędnych szerokości i długości geograficznej na ciąg zakodowany w [Geohash](https://en.wikipedia.org/wiki/Geohash).

## Składnia Analyze

```python
func.geohash_encode(lon, lat)
```

## Przykłady Analyze

```python
func.geohash_encode(-5.60302734375, 42.593994140625)

┌─────────────────────────────────────────────────────────┐
│ func.geohash_encode((- 5.60302734375), 42.593994140625) │
├─────────────────────────────────────────────────────────┤
│ ezs42d000000                                            │
└─────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
GEOHASH_ENCODE(lon, lat)
```

## Przykłady SQL

```sql
SELECT GEOHASH_ENCODE(-5.60302734375, 42.593994140625);

┌────────────────────────────────────────────────────┐
│ geohash_encode((- 5.60302734375), 42.593994140625) │
├────────────────────────────────────────────────────┤
│ ezs42d000000                                       │
└────────────────────────────────────────────────────┘
```
