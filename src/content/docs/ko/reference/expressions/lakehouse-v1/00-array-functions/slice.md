---
title: SLICE (Lakehouse v1)
description: SLICE — 인덱스(1부터 시작)로 배열에서 슬라이스를 추출합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/slice.md
---

인덱스(1부터 시작)로 배열에서 슬라이스를 추출합니다.

## Analyze 구문

```python
func.slice( <array>, <start>[, <end>] )
```

## Analyze 예제

```python
func.slice([1, 21, 32, 4], 2, 3)

┌──────────────────────────────────┐
│ func.slice([1, 21, 32, 4], 2, 3) │
├──────────────────────────────────┤
│ [21,32]                          │ 
└──────────────────────────────────┘
```

## SQL 구문

```sql
SLICE( <array>, <start>[, <end>] )
```

## 별칭

- [ARRAY_SLICE](../array-slice)

## SQL 예제

```sql
SELECT ARRAY_SLICE([1, 21, 32, 4], 2, 3), SLICE([1, 21, 32, 4], 2, 3);

┌─────────────────────────────────────────────────────────────────┐
│ array_slice([1, 21, 32, 4], 2, 3) │ slice([1, 21, 32, 4], 2, 3) │
├───────────────────────────────────┼─────────────────────────────┤
│ [21,32]                           │ [21,32]                     │
└─────────────────────────────────────────────────────────────────┘
```
