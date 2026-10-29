---
title: ARRAY_LENGTH (Lakehouse v1)
description: ARRAY_LENGTH — 배열의 길이를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-length.md
---

배열의 길이를 반환합니다.

## Analyze 구문

```python
func.array_length( <array> )
```

## Analyze 예제

```python
func.array_length([1, 2])

┌────────────────────────────┐
│ func.array_length([1, 2])  │
├────────────────────────────┤
│                          2 │
└────────────────────────────┘
```

## SQL 구문

```sql
ARRAY_LENGTH( <array> )
```

## SQL 예제

```sql
SELECT ARRAY_LENGTH([1, 2]);

┌──────────────────────┐
│ array_length([1, 2]) │
├──────────────────────┤
│                    2 │
└──────────────────────┘
```
