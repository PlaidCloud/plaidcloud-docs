---
title: CBRT (Lakehouse v2)
description: CBRT — 숫자의 세제곱근을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cbrt.md
---

숫자의 세제곱근을 반환합니다.

## Analyze 구문

```python
func.cbrt(<x>)
```

## Analyze 예제

```python
func.cbrt(27)

┌─────┐
│ 3.0  │
└─────┘
```

## SQL 구문

```sql
CBRT(<x>)
```

## SQL 예제

```sql
SELECT CBRT(27);

┌─────┐
│ 3.0  │
└─────┘
```
