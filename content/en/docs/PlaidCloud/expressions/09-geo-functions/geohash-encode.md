---
title: GEOHASH_ENCODE
---

Converts a pair of latitude and longitude coordinates into a [Geohash](https://en.wikipedia.org/wiki/Geohash)-encoded string.

## SQL Syntax

```sql
GEOHASH_ENCODE(lon, lat)
```

## SQL Examples

```sql
SELECT GEOHASH_ENCODE(-5.60302734375, 42.593994140625);

┌────────────────────────────────────────────────────┐
│ geohash_encode((- 5.60302734375), 42.593994140625) │
├────────────────────────────────────────────────────┤
│ ezs42d000000                                       │
└────────────────────────────────────────────────────┘
```