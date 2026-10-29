---
title: ARRAY_CONCAT (Lakehouse v1)
description: ARRAY_CONCAT — 두 배열을 연결합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-concat.md
---

두 배열을 연결합니다.

## Analyze 구문

```python
func.array_concat( <array1>, <array2> )
```

## Analyze 예제

```python
func.array_concat([1, 2], [3, 4])

┌────────────────────────────────────┐
│ func.array_concat([1, 2], [3, 4])  │
├────────────────────────────────────┤
│ [1,2,3,4]                          │
└────────────────────────────────────┘
```

## SQL 구문

```sql
ARRAY_CONCAT( <array1>, <array2> )
```

## SQL 예제

```sql
SELECT ARRAY_CONCAT([1, 2], [3, 4]);

┌──────────────────────────────┐
│ array_concat([1, 2], [3, 4]) │
├──────────────────────────────┤
│ [1,2,3,4]                    │
└──────────────────────────────┘
```
