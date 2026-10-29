---
title: H3_HEX_AREA_KM2 (Lakehouse v1)
description: H3_HEX_AREA_KM2 — 지정한 해상도에서 육각형의 평균 면적을 제곱킬로미터 단위로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-hex-area-km2.md
---

지정한 해상도에서 육각형의 평균 면적을 제곱킬로미터 단위로 반환합니다. 오각형은 제외합니다.

## Analyze 구문

```python
func.h3_area_km2(res)
```

## Analyze 예제

```python
func.h3_area_km2(1)

┌─────────────────────────┐
│ func.h3_hex_area_km2(1) │
├─────────────────────────┤
│       609788.4417941332 │
└─────────────────────────┘
```

## SQL 구문

```sql
H3_HEX_AREA_KM2(res)
```

## SQL 예제

```sql
SELECT H3_HEX_AREA_KM2(1);

┌────────────────────┐
│ h3_hex_area_km2(1) │
├────────────────────┤
│  609788.4417941332 │
└────────────────────┘
```
