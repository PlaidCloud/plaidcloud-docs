---
title: ARRAY_TO_BITMAP (Lakehouse v2)
description: ARRAY_TO_BITMAP — 정수 배열을 비트맵으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-to-bitmap.md
---

정수 배열을 비트맵으로 변환합니다.

## Analyze 구문

```python
func.array_to_bitmap([1, 2, 3])
```

## Analyze 예제

```python
func.array_to_bitmap([1, 2, 3])

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 구문

```sql
ARRAY_TO_BITMAP([1, 2, 3])
```

## SQL 예제

```sql
SELECT BITMAP_TO_STRING(ARRAY_TO_BITMAP([1, 2, 3]));

┌───────┐
│ 1,2,3 │
└───────┘
```
