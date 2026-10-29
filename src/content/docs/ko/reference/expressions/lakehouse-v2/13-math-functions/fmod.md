---
title: FMOD (Lakehouse v2)
description: FMOD — 두 숫자를 나눈 부동 소수점 나머지를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/fmod.md
---

두 숫자를 나눈 부동 소수점 나머지를 반환합니다.

## Analyze 구문

```python
func.fmod(<x>, <y>)
```

## Analyze 예제

```python
func.fmod(10.5, 3.0)

┌─────┐
│ 1.5  │
└─────┘
```

## SQL 구문

```sql
FMOD(<x>, <y>)
```

## SQL 예제

```sql
SELECT FMOD(10.5, 3.0);

┌─────┐
│ 1.5  │
└─────┘
```
