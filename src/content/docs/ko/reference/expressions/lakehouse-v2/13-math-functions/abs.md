---
title: ABS (Lakehouse v2)
description: ABS — 숫자의 절댓값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/abs.md
---

숫자의 절댓값을 반환합니다.

## Analyze 구문

```python
func.abs(<x>)
```

## Analyze 예제

```python
func.abs(-5)

┌───┐
│ 5  │
└───┘
```

## SQL 구문

```sql
ABS(<x>)
```

## SQL 예제

```sql
SELECT ABS(-5);

┌───┐
│ 5  │
└───┘
```
