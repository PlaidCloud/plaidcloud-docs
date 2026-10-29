---
title: TO_VARIANT (Lakehouse v1)
description: TO_VARIANT — 값을 VARIANT 데이터 형식으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-variant.md
---

값을 VARIANT 데이터 형식으로 변환합니다.

## Analyze 구문

```python
func.to_variant( <expr> )
```

## Analyze 예제

```python
func.to_variant(to_bitmap('100,200,300'))

┌───────────────────────────────────────────┐
│ func.to_variant(to_bitmap('100,200,300')) │
├───────────────────────────────────────────┤
│ [100,200,300]                             │
└───────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_VARIANT( <expr> )
```

## SQL 예제

```sql
SELECT TO_VARIANT(TO_BITMAP('100,200,300'));

┌──────────────────────────────────────┐
│ to_variant(to_bitmap('100,200,300')) │
├──────────────────────────────────────┤
│ [100,200,300]                        │
└──────────────────────────────────────┘
```
