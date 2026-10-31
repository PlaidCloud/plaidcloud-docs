---
title: ARRAY_PREPEND (Lakehouse v1)
description: ARRAY_PREPEND — 배열의 앞에 요소를 추가합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-prepend.md
---

배열의 앞에 요소를 추가합니다.

## Analyze 구문

```python
func.array_prepend( <element>, <array> )
```

## Analyze 예제

```python
func.array_prepend(1, [3, 4])

┌────────────────────────────────┐
│ func.array_prepend(1, [3, 4])  │
├────────────────────────────────┤
│ [1,3,4]                        │
└────────────────────────────────┘
```

## SQL 구문

```sql
ARRAY_PREPEND( <element>, <array> )
```

## SQL 예제

```sql
SELECT ARRAY_PREPEND(1, [3, 4]);

┌──────────────────────────┐
│ array_prepend(1, [3, 4]) │
├──────────────────────────┤
│ [1,3,4]                  │
└──────────────────────────┘
```
