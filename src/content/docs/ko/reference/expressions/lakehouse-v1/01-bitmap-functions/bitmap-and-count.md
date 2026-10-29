---
title: BITMAP_AND_COUNT (Lakehouse v1)
description: BITMAP_AND_COUNT — 논리 AND 연산을 수행하여 비트맵에서 1로 설정된 비트의 수를 셉니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-and-count.md
---

논리 AND 연산을 수행하여 비트맵에서 1로 설정된 비트의 수를 셉니다.

## Analyze 구문

```python
func.bitmap_and_count( <bitmap> )
```

## Analyze 예제

```python
func.bitmap_and_count(to_bitmap('1, 3, 5'))

┌─────────────────────────────────────────────┐
│ func.bitmap_and_count(to_bitmap('1, 3, 5')) │
├─────────────────────────────────────────────┤
│                                           3 │
└─────────────────────────────────────────────┘
```

## SQL 구문

```sql
BITMAP_AND_COUNT( <bitmap> )
```

## SQL 예제

```sql
SELECT BITMAP_AND_COUNT(TO_BITMAP('1, 3, 5'));

┌────────────────────────────────────────┐
│ bitmap_and_count(to_bitmap('1, 3, 5')) │
├────────────────────────────────────────┤
│                                      3 │
└────────────────────────────────────────┘
```
