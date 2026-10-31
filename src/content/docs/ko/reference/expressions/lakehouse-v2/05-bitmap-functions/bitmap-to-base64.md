---
title: BITMAP_TO_BASE64 (Lakehouse v2)
description: BITMAP_TO_BASE64 — 비트맵을 base64로 인코딩된 문자열로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-base64.md
---

비트맵을 base64로 인코딩된 문자열로 변환합니다.

## Analyze 구문

```python
func.bitmap_to_base64(<bitmap>)
```

## Analyze 예제

```python
func.bitmap_to_base64(get_column(table, 'bm'))

┌──────────┐
│ 'AQI...' │
└──────────┘
```

## SQL 구문

```sql
BITMAP_TO_BASE64(<bitmap>)
```

## SQL 예제

```sql
SELECT BITMAP_TO_BASE64(BITMAP_FROM_STRING('1,2,3'));

┌─────────────────┐
│ (base64 string) │
└─────────────────┘
```
