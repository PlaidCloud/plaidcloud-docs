---
title: ROUND (Lakehouse v2)
description: ROUND — 숫자를 지정한 소수 자릿수로 반올림합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/round.md
---

숫자를 지정한 소수 자릿수로 반올림합니다.

## Analyze 구문

```python
func.round(<x>[, <d>])
```

## Analyze 예제

```python
func.round(3.14159, 2)

┌──────┐
│ 3.14  │
└──────┘
```

## SQL 구문

```sql
ROUND(<x>[, <d>])
```

## SQL 예제

```sql
SELECT ROUND(3.14159, 2);

┌──────┐
│ 3.14  │
└──────┘
```
