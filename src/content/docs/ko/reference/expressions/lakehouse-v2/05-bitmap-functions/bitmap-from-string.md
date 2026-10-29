---
title: BITMAP_FROM_STRING (Lakehouse v2)
description: BITMAP_FROM_STRING — 쉼표로 구분된 정수 문자열을 비트맵으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-from-string.md
---

쉼표로 구분된 정수 문자열을 비트맵으로 변환합니다.

## Analyze 구문

```python
func.bitmap_from_string(<str>)
```

## Analyze 예제

```python
func.bitmap_from_string('1,2,3,4,5')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 구문

```sql
BITMAP_FROM_STRING(<str>)
```

## SQL 예제

```sql
SELECT BITMAP_COUNT(BITMAP_FROM_STRING('1,2,3,4,5'));

┌───┐
│ 5 │
└───┘
```
