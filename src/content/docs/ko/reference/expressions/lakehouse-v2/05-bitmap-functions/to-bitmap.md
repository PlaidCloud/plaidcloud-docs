---
title: TO_BITMAP (Lakehouse v2)
description: TO_BITMAP — 정수 값을 해당 값 하나만 담은 비트맵으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/to-bitmap.md
---

정수 값을 해당 값 하나만 담은 비트맵으로 변환합니다.

## Analyze 구문

```python
func.to_bitmap(<value>)
```

## Analyze 예제

```python
func.to_bitmap(42)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 구문

```sql
TO_BITMAP(<value>)
```

## SQL 예제

```sql
SELECT BITMAP_TO_STRING(TO_BITMAP(42));

┌────┐
│ 42 │
└────┘
```
