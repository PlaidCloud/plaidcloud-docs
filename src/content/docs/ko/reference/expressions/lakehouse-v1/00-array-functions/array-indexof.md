---
title: ARRAY_INDEXOF (Lakehouse v1)
description: ARRAY_INDEXOF — 배열에 요소가 있으면 해당 요소의 인덱스(1부터 시작)를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-indexof.md
---

배열에 요소가 있으면 해당 요소의 인덱스(1부터 시작)를 반환합니다.

## Analyze 구문

```python
func.array_indexof( <array>, <element> )
```

## Analyze 예제

```python
func.array_indexof([1, 2, 9], 9)

┌───────────────────────────────────┐
│ func.array_indexof([1, 2, 9], 9)  │
├───────────────────────────────────┤
│                                 3 │
└───────────────────────────────────┘
```

## SQL 구문

```sql
ARRAY_INDEXOF( <array>, <element> )
```

## SQL 예제

```sql
SELECT ARRAY_INDEXOF([1, 2, 9], 9);

┌─────────────────────────────┐
│ array_indexof([1, 2, 9], 9) │
├─────────────────────────────┤
│                           3 │
└─────────────────────────────┘
```
