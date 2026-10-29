---
title: LN (Lakehouse v2)
description: LN — 숫자의 자연로그를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ln.md
---

숫자의 자연로그를 반환합니다.

## Analyze 구문

```python
func.ln(<x>)
```

## Analyze 예제

```python
func.ln(2.718281828459045)

┌─────┐
│ 1.0  │
└─────┘
```

## SQL 구문

```sql
LN(<x>)
```

## SQL 예제

```sql
SELECT LN(EXP(1));

┌─────┐
│ 1.0  │
└─────┘
```
