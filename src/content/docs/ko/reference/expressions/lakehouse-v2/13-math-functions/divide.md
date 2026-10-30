---
title: DIVIDE (Lakehouse v2)
description: DIVIDE — 한 숫자를 다른 숫자로 나눈 결과를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/divide.md
---

한 숫자를 다른 숫자로 나눈 결과를 반환합니다.

## Analyze 구문

```python
func.divide(<x>, <y>)
```

## Analyze 예제

```python
func.divide(10, 3)

┌────────────────────┐
│ 3.3333333333333335  │
└────────────────────┘
```

## SQL 구문

```sql
DIVIDE(<x>, <y>)
```

## SQL 예제

```sql
SELECT DIVIDE(10, 3);

┌────────────────────┐
│ 3.3333333333333335  │
└────────────────────┘
```
