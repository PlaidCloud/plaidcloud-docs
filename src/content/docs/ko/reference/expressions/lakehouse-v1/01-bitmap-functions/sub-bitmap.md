---
title: SUB_BITMAP (Lakehouse v1)
description: SUB_BITMAP — 시작 인덱스부터 지정한 크기만큼 원본 비트맵의 하위 비트맵을 생성합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/sub-bitmap.md
---

시작 인덱스부터 지정한 크기만큼 원본 비트맵의 하위 비트맵을 생성합니다.

## Analyze 구문

```python
func.sub_bitmap( <bitmap>, <start>, <size> )
```

## Analyze 예제

```python
func.sub_bitmap(func.build_bitmap([1, 2, 3, 4, 5]), 1, 3)

┌───────────────────────────────────────────────────────────┐
│ func.sub_bitmap(func.build_bitmap([1, 2, 3, 4, 5]), 1, 3) │
├───────────────────────────────────────────────────────────┤
│ 2,3,4                                                     │
└───────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
SUB_BITMAP( <bitmap>, <start>, <size> )
```

## SQL 예제

```sql
SELECT SUB_BITMAP(BUILD_BITMAP([1, 2, 3, 4, 5]), 1, 3)::String;

┌─────────────────────────────────────────────────────────┐
│ sub_bitmap(build_bitmap([1, 2, 3, 4, 5]), 1, 3)::string │
├─────────────────────────────────────────────────────────┤
│ 2,3,4                                                   │
└─────────────────────────────────────────────────────────┘
```
