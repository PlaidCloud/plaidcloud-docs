---
title: SIN (Lakehouse v2)
description: SIN — 라디안 단위 숫자의 사인을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sin.md
---

라디안 단위 숫자의 사인을 반환합니다.

## Analyze 구문

```python
func.sin(<x>)
```

## Analyze 예제

```python
func.sin(0)

┌─────┐
│ 0.0  │
└─────┘
```

## SQL 구문

```sql
SIN(<x>)
```

## SQL 예제

```sql
SELECT SIN(0);

┌─────┐
│ 0.0  │
└─────┘
```
