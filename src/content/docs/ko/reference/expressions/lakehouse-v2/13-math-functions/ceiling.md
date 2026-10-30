---
title: CEILING (Lakehouse v2)
description: CEILING — 숫자보다 크거나 같은 가장 작은 정수를 반환합니다. `CEIL`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ceiling.md
---

숫자보다 크거나 같은 가장 작은 정수를 반환합니다. `CEIL`의 별칭입니다.

## Analyze 구문

```python
func.ceiling(<x>)
```

## Analyze 예제

```python
func.ceiling(3.2)

┌───┐
│ 4  │
└───┘
```

## SQL 구문

```sql
CEILING(<x>)
```

## SQL 예제

```sql
SELECT CEILING(3.2);

┌───┐
│ 4  │
└───┘
```
