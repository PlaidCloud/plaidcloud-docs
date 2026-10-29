---
title: CEIL (Lakehouse v2)
description: CEIL — 숫자보다 크거나 같은 가장 작은 정수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ceil.md
---

숫자보다 크거나 같은 가장 작은 정수를 반환합니다.

## Analyze 구문

```python
func.ceil(<x>)
```

## Analyze 예제

```python
func.ceil(3.2)

┌───┐
│ 4  │
└───┘
```

## SQL 구문

```sql
CEIL(<x>)
```

## SQL 예제

```sql
SELECT CEIL(3.2);

┌───┐
│ 4  │
└───┘
```
