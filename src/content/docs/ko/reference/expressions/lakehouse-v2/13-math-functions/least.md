---
title: LEAST (Lakehouse v2)
description: LEAST — 값 목록에서 가장 작은 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/least.md
---

값 목록에서 가장 작은 값을 반환합니다.

## Analyze 구문

```python
func.least(<val1>, <val2>[, ...])
```

## Analyze 예제

```python
func.least(3, 7, 1, 9, 4)

┌───┐
│ 1  │
└───┘
```

## SQL 구문

```sql
LEAST(<val1>, <val2>[, ...])
```

## SQL 예제

```sql
SELECT LEAST(3, 7, 1, 9, 4);

┌───┐
│ 1  │
└───┘
```
