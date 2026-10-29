---
title: MULTIPLY (Lakehouse v2)
description: MULTIPLY — 두 숫자의 곱을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/multiply.md
---

두 숫자의 곱을 반환합니다.

## Analyze 구문

```python
func.multiply(<x>, <y>)
```

## Analyze 예제

```python
func.multiply(6, 7)

┌────┐
│ 42  │
└────┘
```

## SQL 구문

```sql
MULTIPLY(<x>, <y>)
```

## SQL 예제

```sql
SELECT MULTIPLY(6, 7);

┌────┐
│ 42  │
└────┘
```
