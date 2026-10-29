---
title: H3_IS_VALID (Lakehouse v1)
description: H3_IS_VALID — 지정한 H3 인덱스가 유효한지 확인합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-is-valid.md
---

지정한 [H3](https://eng.uber.com/h3/) 인덱스가 유효한지 확인합니다.

## Analyze 구문

```python
func.h3_is_valid(h3)
```

## Analyze 예제

```python
func.h3_is_valid(644325524701193974)

┌──────────────────────────────────────┐
│ func.h3_is_valid(644325524701193974) │
├──────────────────────────────────────┤
│ true                                 │
└──────────────────────────────────────┘
```

## SQL 구문

```sql
H3_IS_VALID(h3)
```

## SQL 예제

```sql
SELECT H3_IS_VALID(644325524701193974);

┌─────────────────────────────────┐
│ h3_is_valid(644325524701193974) │
├─────────────────────────────────┤
│ true                            │
└─────────────────────────────────┘
```
