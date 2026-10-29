---
title: TO_BITMAP (Lakehouse v1)
description: TO_BITMAP — 값을 BITMAP 데이터 형식으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-bitmap.md
---

값을 BITMAP 데이터 형식으로 변환합니다.

## Analyze 구문

```python
func.to_bitmap( <expr> )
```

## Analyze 예제

```python
func.to_bitmap('1101')

┌─────────────────────────┐
│ func.to_bitmap('1101')  │
├─────────────────────────┤
│ <bitmap binary>         │
└─────────────────────────┘
```

## SQL 구문

```sql
TO_BITMAP( <expr> )
```

## SQL 예제

```sql
SELECT TO_BITMAP('1101');

┌───────────────────┐
│ to_bitmap('1101') │
├───────────────────┤
│ <bitmap binary>   │
└───────────────────┘
```
