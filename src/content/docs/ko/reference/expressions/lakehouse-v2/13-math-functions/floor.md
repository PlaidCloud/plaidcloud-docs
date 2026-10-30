---
title: FLOOR (Lakehouse v2)
description: FLOOR — 숫자보다 작거나 같은 가장 큰 정수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/floor.md
---

숫자보다 작거나 같은 가장 큰 정수를 반환합니다.

## Analyze 구문

```python
func.floor(<x>)
```

## Analyze 예제

```python
func.floor(3.7)

┌───┐
│ 3  │
└───┘
```

## SQL 구문

```sql
FLOOR(<x>)
```

## SQL 예제

```sql
SELECT FLOOR(3.7);

┌───┐
│ 3  │
└───┘
```
