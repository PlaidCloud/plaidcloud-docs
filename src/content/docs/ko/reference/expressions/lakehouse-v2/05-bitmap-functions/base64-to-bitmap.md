---
title: BASE64_TO_BITMAP (Lakehouse v2)
description: BASE64_TO_BITMAP — base64로 인코딩된 문자열을 비트맵으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/base64-to-bitmap.md
---

base64로 인코딩된 문자열을 비트맵으로 변환합니다.

## Analyze 구문

```python
func.base64_to_bitmap(<str>)
```

## Analyze 예제

```python
func.base64_to_bitmap(get_column(table, 'b64_col'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 구문

```sql
BASE64_TO_BITMAP(<str>)
```

## SQL 예제

```sql
SELECT BITMAP_TO_STRING(BASE64_TO_BITMAP(b64_col)) FROM data;

┌───────┐
│ 1,2,3 │
└───────┘
```
