---
title: ARRAY_GENERATE (Lakehouse v2)
description: ARRAY_GENERATE — 연속된 값으로 이루어진 배열을 생성합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-generate.md
---

연속된 값으로 이루어진 배열을 생성합니다.

## Analyze 구문

```python
func.array_generate(1, 5)
```

## Analyze 예제

```python
func.array_generate(1, 5)

┌─────────────┐
│ [1,2,3,4,5] │
└─────────────┘
```

## SQL 구문

```sql
ARRAY_GENERATE(1, 5)
```

## SQL 예제

```sql
SELECT ARRAY_GENERATE(1, 5);

┌─────────────┐
│ [1,2,3,4,5] │
└─────────────┘
```
