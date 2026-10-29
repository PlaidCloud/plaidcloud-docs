---
title: BUILD_BITMAP (Lakehouse v1)
description: BUILD_BITMAP — 양의 정수 배열을 BITMAP 값으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/build-bitmap.md
---

양의 정수 배열을 BITMAP 값으로 변환합니다.


## Analyze 구문

```python
func.build_bitmap( <expr> )
```

## Analyze 예제

```python
func.to_string(func.build_bitmap([1, 4, 5]))

┌───────────────────────────────────────────────┐
│ func.to_string(func.build_bitmap([1, 4, 5]))  │
├───────────────────────────────────────────────┤
│ 1,4,5                                         │
└───────────────────────────────────────────────┘
```

## SQL 구문

```sql
BUILD_BITMAP( <expr> )
```

## SQL 예제

```sql
SELECT BUILD_BITMAP([1,4,5])::String;

┌─────────────────────────────────┐
│ build_bitmap([1, 4, 5])::string │
├─────────────────────────────────┤
│ 1,4,5                           │
└─────────────────────────────────┘
```
