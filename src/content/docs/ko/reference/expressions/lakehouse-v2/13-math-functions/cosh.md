---
title: COSH (Lakehouse v2)
description: COSH — 숫자의 쌍곡코사인을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cosh.md
---

숫자의 쌍곡코사인을 반환합니다.

## Analyze 구문

```python
func.cosh(<x>)
```

## Analyze 예제

```python
func.cosh(0)

┌─────┐
│ 1.0  │
└─────┘
```

## SQL 구문

```sql
COSH(<x>)
```

## SQL 예제

```sql
SELECT COSH(0);

┌─────┐
│ 1.0  │
└─────┘
```
