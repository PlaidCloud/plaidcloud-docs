---
title: ARRAY_SORT (Lakehouse v1)
description: ARRAY_SORT — 배열의 요소를 오름차순으로 정렬합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-sort.md
---

배열의 요소를 오름차순으로 정렬합니다.

## Analyze 구문

```sql
func.array_sort( <array>[, <order>, <nullposition>] )
```

| 매개변수 | 기본값 | 설명 |
|--------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| order | ASC | 정렬 순서를 오름차순(ASC) 또는 내림차순(DESC)으로 지정합니다. |
| nullposition | NULLS FIRST | 정렬 결과에서 NULL 값의 위치를 결정하며, 정렬 출력의 처음(NULLS FIRST) 또는 끝(NULLS LAST)에 둡니다. |

## Analyze 예제

```sql
func.array_sort([1, 4, 3, 2])

┌────────────────────────────────┐
│ func.array_sort([1, 4, 3, 2])  │
├────────────────────────────────┤
│ [1,2,3,4]                      │
└────────────────────────────────┘
```

## SQL 구문

```sql
ARRAY_SORT( <array>[, <order>, <nullposition>] )
```

| 매개변수 | 기본값 | 설명 |
|--------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| order | ASC | 정렬 순서를 오름차순(ASC) 또는 내림차순(DESC)으로 지정합니다. |
| nullposition | NULLS FIRST | 정렬 결과에서 NULL 값의 위치를 결정하며, 정렬 출력의 처음(NULLS FIRST) 또는 끝(NULLS LAST)에 둡니다. |

## SQL 예제

```sql
SELECT ARRAY_SORT([1, 4, 3, 2]);

┌──────────────────────────┐
│ array_sort([1, 4, 3, 2]) │
├──────────────────────────┤
│ [1,2,3,4]                │
└──────────────────────────┘
```
