---
title: RANGE (Lakehouse v1)
description: RANGE — [start, end) 범위의 값을 모은 배열을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/range.md
---

[start, end) 범위의 값을 모은 배열을 반환합니다.

## Analyze 구문

```python
func.range( <start>, <end> )
```

## SQL 예제

```python
func.range(1, 5)

┌────────────────────┐
│  func.range(1, 5)  │
├────────────────────┤
│ [1,2,3,4]          │
└────────────────────┘
```

## SQL 구문

```sql
RANGE( <start>, <end> )
```

## SQL 예제

```sql
SELECT RANGE(1, 5);

┌───────────────┐
│  range(1, 5)  │
├───────────────┤
│ [1,2,3,4]     │
└───────────────┘
```
