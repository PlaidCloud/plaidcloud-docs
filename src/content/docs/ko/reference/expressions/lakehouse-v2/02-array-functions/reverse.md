---
title: "REVERSE (Array, Lakehouse v2)"
description: REVERSE — 요소의 순서를 뒤집은 배열을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/reverse.md
---

요소의 순서를 뒤집은 배열을 반환합니다.

## Analyze 구문

```python
func.reverse([1, 2, 3])
```

## Analyze 예제

```python
func.reverse([1, 2, 3])

┌─────────┐
│ [3,2,1] │
└─────────┘
```

## SQL 구문

```sql
REVERSE([1, 2, 3])
```

## SQL 예제

```sql
SELECT ARRAY_REVERSE([1, 2, 3]);

┌─────────┐
│ [3,2,1] │
└─────────┘
```
