---
title: H3_CELL_AREA_M2 (Lakehouse v1)
description: H3_CELL_AREA_M2 — 특정 셀의 정확한 면적을 제곱미터 단위로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-cell-area-m2.md
---

특정 셀의 정확한 면적을 제곱미터 단위로 반환합니다.

## Analyze 구문

```python
func.h3_cell_area_m2(h3)
```

## Analyze 예제

```python
func.h3_cell_area_m2(599119489002373119)

┌──────────────────────────────────────────┐
│ func.h3_cell_area_m2(599119489002373119) │
├──────────────────────────────────────────┤
│                       127785582.60809991 │
└──────────────────────────────────────────┘
```

## SQL 구문

```sql
H3_CELL_AREA_M2(h3)
```

## SQL 예제

```sql
SELECT H3_CELL_AREA_M2(599119489002373119);

┌─────────────────────────────────────┐
│ h3_cell_area_m2(599119489002373119) │
├─────────────────────────────────────┤
│                  127785582.60809991 │
└─────────────────────────────────────┘
```
