---
title: ARRAY_REPEAT (Lakehouse v2)
description: ARRAY_REPEAT — 지정한 요소를 N번 반복한 배열을 생성합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-repeat.md
---

지정한 요소를 N번 반복한 배열을 생성합니다.

## Analyze 구문

```python
func.array_repeat('x', 3)
```

## Analyze 예제

```python
func.array_repeat('x', 3)

┌───────────────┐
│ ['x','x','x'] │
└───────────────┘
```

## SQL 구문

```sql
ARRAY_REPEAT('x', 3)
```

## SQL 예제

```sql
SELECT ARRAY_REPEAT('x', 3);

┌───────────────┐
│ ["x","x","x"] │
└───────────────┘
```
