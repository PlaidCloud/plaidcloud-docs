---
title: H3_GET_BASE_CELL (Lakehouse v1)
description: H3_GET_BASE_CELL — 지정한 H3 인덱스의 기본 셀 번호를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-base-cell.md
---

지정한 [H3](https://eng.uber.com/h3/) 인덱스의 기본 셀 번호를 반환합니다. 

## Analyze 구문

```python
func.h3_get_base_cell(h3)
```

## Analyze 예제

```python
func.h3_get_base_cell(644325524701193974)

┌───────────────────────────────────────────┐
│ func.h3_get_base_cell(644325524701193974) │
├───────────────────────────────────────────┤
│                                         8 │
└───────────────────────────────────────────┘
```

## SQL 구문

```sql
H3_GET_BASE_CELL(h3)
```

## SQL 예제

```sql
SELECT H3_GET_BASE_CELL(644325524701193974);

┌──────────────────────────────────────┐
│ h3_get_base_cell(644325524701193974) │
├──────────────────────────────────────┤
│                                    8 │
└──────────────────────────────────────┘
```
