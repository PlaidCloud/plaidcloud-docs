---
title: GEO_TO_H3 (Lakehouse v1)
description: GEO_TO_H3 — 지정한 위치가 속한 육각형 셀의 H3 인덱스를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/geo-to-h3.md
---

지정한 위치가 속한 육각형 셀의 [H3](https://eng.uber.com/h3/) 인덱스를 반환합니다. 0을 반환하면 오류가 발생한 것입니다.

## Analyze 구문

```python
func.geo_to_h3(lon, lat, res)
```

## Analyze 예제

```python
func.geo_to_h3(37.79506683, 55.71290588, 15)

┌──────────────────────────────────────────────┐
│ func.geo_to_h3(37.79506683, 55.71290588, 15) │
├──────────────────────────────────────────────┤
│                           644325524701193974 │
└──────────────────────────────────────────────┘
```

## SQL 구문

```sql
GEO_TO_H3(lon, lat, res)
```

## SQL 예제

```sql
SELECT GEO_TO_H3(37.79506683, 55.71290588, 15);

┌─────────────────────────────────────────┐
│ geo_to_h3(37.79506683, 55.71290588, 15) │
├─────────────────────────────────────────┤
│                      644325524701193974 │
└─────────────────────────────────────────┘
```
