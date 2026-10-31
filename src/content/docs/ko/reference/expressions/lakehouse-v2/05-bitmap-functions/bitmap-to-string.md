---
title: BITMAP_TO_STRING (Lakehouse v2)
description: BITMAP_TO_STRING — 비트맵을 쉼표로 구분된 문자열로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-string.md
---

비트맵을 쉼표로 구분된 문자열로 변환합니다.

## Analyze 구문

```python
func.bitmap_to_string(<bitmap>)
```

## Analyze 예제

```python
func.bitmap_to_string(get_column(table, 'bm'))

┌─────────┐
│ '1,2,3' │
└─────────┘
```

## SQL 구문

```sql
BITMAP_TO_STRING(<bitmap>)
```

## SQL 예제

```sql
SELECT BITMAP_TO_STRING(BITMAP_FROM_STRING('1,2,3'));

┌───────┐
│ 1,2,3 │
└───────┘
```
