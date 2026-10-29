---
title: SQUARE (Lakehouse v2)
description: SQUARE — 숫자의 제곱을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/square.md
---

숫자의 제곱을 반환합니다.

## Analyze 구문

```python
func.square(<x>)
```

## Analyze 예제

```python
func.square(7)

┌────┐
│ 49  │
└────┘
```

## SQL 구문

```sql
SQUARE(<x>)
```

## SQL 예제

```sql
SELECT SQUARE(7);

┌────┐
│ 49  │
└────┘
```
