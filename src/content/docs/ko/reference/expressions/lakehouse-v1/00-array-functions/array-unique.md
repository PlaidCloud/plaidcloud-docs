---
title: ARRAY_UNIQUE (Lakehouse v1)
description: ARRAY_UNIQUE — 배열에서 고유한 요소(NULL 제외)의 개수를 셉니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-unique.md
---

배열에서 고유한 요소(NULL 제외)의 개수를 셉니다.

## Analyze 구문

```python
func.array_unique( <array> )
```

## Analyze 예제

```python
func.array_unique([1, 2, 3, 3, 4])

┌─────────────────────────────────────┐
│ func.array_unique([1, 2, 3, 3, 4])  │
├─────────────────────────────────────┤
│                                   4 │
└─────────────────────────────────────┘
```

## SQL 구문

```sql
ARRAY_UNIQUE( <array> )
```

## SQL 예제

```sql
SELECT ARRAY_UNIQUE([1, 2, 3, 3, 4]);

┌───────────────────────────────┐
│ array_unique([1, 2, 3, 3, 4]) │
├───────────────────────────────┤
│                             4 │
└───────────────────────────────┘
```
