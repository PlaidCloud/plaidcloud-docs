---
title: GEOHASH_ENCODE (Lakehouse v1)
description: GEOHASH_ENCODE — wandelt ein Paar aus Breiten- und Längengradkoordinaten in eine Geohash-codierte Zeichenfolge um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geohash-encode.md
---

Wandelt ein Paar aus Breiten- und Längengradkoordinaten in eine [Geohash](https://en.wikipedia.org/wiki/Geohash)-codierte Zeichenfolge um.

## Analyze-Syntax

```python
func.geohash_encode(lon, lat)
```

## Analyze-Beispiele

```python
func.geohash_encode(-5.60302734375, 42.593994140625)

┌─────────────────────────────────────────────────────────┐
│ func.geohash_encode((- 5.60302734375), 42.593994140625) │
├─────────────────────────────────────────────────────────┤
│ ezs42d000000                                            │
└─────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
GEOHASH_ENCODE(lon, lat)
```

## SQL-Beispiele

```sql
SELECT GEOHASH_ENCODE(-5.60302734375, 42.593994140625);

┌────────────────────────────────────────────────────┐
│ geohash_encode((- 5.60302734375), 42.593994140625) │
├────────────────────────────────────────────────────┤
│ ezs42d000000                                       │
└────────────────────────────────────────────────────┘
```
