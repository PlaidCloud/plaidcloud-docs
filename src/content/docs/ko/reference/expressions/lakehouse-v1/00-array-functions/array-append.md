---
title: ARRAY_APPEND (Lakehouse v1)
description: ARRAY_APPEND — 배열의 앞에 요소를 추가합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-append.md
---

배열의 앞에 요소를 추가합니다.

## Analyze 구문

```python
func.array_append( <array>, <element>)
```

## Analyze 예제

```python
func.array_append([3, 4], 5)

┌──────────────────────────────┐
│ func.array_append([3, 4], 5) │
├──────────────────────────────┤
│ [3,4,5]                      │
└──────────────────────────────┘
```

## SQL 구문

```sql
ARRAY_APPEND( <array>, <element>)
```

## SQL 예제

```sql
SELECT ARRAY_APPEND([3, 4], 5);

┌─────────────────────────┐
│ array_append([3, 4], 5) │
├─────────────────────────┤
│ [3,4,5]                 │
└─────────────────────────┘
```
