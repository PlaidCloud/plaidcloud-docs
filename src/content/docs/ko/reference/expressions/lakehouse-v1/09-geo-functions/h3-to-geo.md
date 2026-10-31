---
title: H3_TO_GEO (Lakehouse v1)
description: H3_TO_GEO — 지정한 H3 인덱스에 해당하는 경도와 위도를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-geo.md
---

지정한 [H3](https://eng.uber.com/h3/) 인덱스에 해당하는 경도와 위도를 반환합니다. 

## Analyze 구문

```python
func.h3_to_geo(h3)
```

## Analyze 예제

```python
func.h3_to_geo(644325524701193974)

┌────────────────────────────────────────┐
│   func.h3_to_geo(644325524701193974)   │
├────────────────────────────────────────┤
│ (37.79506616830255,55.712902431456676) │
└────────────────────────────────────────┘
```

## SQL 구문

```sql
H3_TO_GEO(h3)
```

## SQL 예제

```sql
SELECT H3_TO_GEO(644325524701193974);

┌────────────────────────────────────────┐
│      h3_to_geo(644325524701193974)     │
├────────────────────────────────────────┤
│ (37.79506616830255,55.712902431456676) │
└────────────────────────────────────────┘
```
