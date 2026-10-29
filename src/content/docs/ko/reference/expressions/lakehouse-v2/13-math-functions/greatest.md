---
title: GREATEST (Lakehouse v2)
description: GREATEST — 값 목록에서 가장 큰 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/greatest.md
---

값 목록에서 가장 큰 값을 반환합니다.

## Analyze 구문

```python
func.greatest(<val1>, <val2>[, ...])
```

## Analyze 예제

```python
func.greatest(3, 7, 1, 9, 4)

┌───┐
│ 9  │
└───┘
```

## SQL 구문

```sql
GREATEST(<val1>, <val2>[, ...])
```

## SQL 예제

```sql
SELECT GREATEST(3, 7, 1, 9, 4);

┌───┐
│ 9  │
└───┘
```
