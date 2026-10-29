---
title: SIGN (Lakehouse v2)
description: "SIGN — 숫자의 부호를 -1, 0 또는 1로 반환합니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sign.md
---

숫자의 부호를 -1, 0 또는 1로 반환합니다.

## Analyze 구문

```python
func.sign(<x>)
```

## Analyze 예제

```python
func.sign(-42)

┌────┐
│ -1  │
└────┘
```

## SQL 구문

```sql
SIGN(<x>)
```

## SQL 예제

```sql
SELECT SIGN(-42);

┌────┐
│ -1  │
└────┘
```
