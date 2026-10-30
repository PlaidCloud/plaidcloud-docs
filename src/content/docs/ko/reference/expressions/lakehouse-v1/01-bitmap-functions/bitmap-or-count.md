---
title: BITMAP_OR_COUNT (Lakehouse v1)
description: BITMAP_OR_COUNT — 논리 OR 연산을 수행하여 비트맵에서 1로 설정된 비트의 수를 셉니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-or-count.md
---

논리 OR 연산을 수행하여 비트맵에서 1로 설정된 비트의 수를 셉니다.

## Analyze 구문

```python
func.bitmap_or_count( <bitmap> )
```

## Analyze 예제

```python
func.bitmap_or_count(func.to_bitmap('1, 3, 5'))

┌─────────────────────────────────────────────────┐
│ func.bitmap_or_count(func.to_bitmap('1, 3, 5')) │
├─────────────────────────────────────────────────┤
│                                               3 │
└─────────────────────────────────────────────────┘
```

## SQL 구문

```sql
BITMAP_OR_COUNT( <bitmap> )
```

## SQL 예제

```sql
SELECT BITMAP_OR_COUNT(TO_BITMAP('1, 3, 5'));

┌───────────────────────────────────────┐
│ bitmap_or_count(to_bitmap('1, 3, 5')) │
├───────────────────────────────────────┤
│                                     3 │
└───────────────────────────────────────┘
```
