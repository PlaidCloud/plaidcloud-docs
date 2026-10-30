---
title: MOD (Lakehouse v2)
description: MOD — 두 숫자를 나눈 나머지를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/mod.md
---

두 숫자를 나눈 나머지를 반환합니다.

## Analyze 구문

```python
func.mod(<x>, <y>)
```

## Analyze 예제

```python
func.mod(10, 3)

┌───┐
│ 1  │
└───┘
```

## SQL 구문

```sql
MOD(<x>, <y>)
```

## SQL 예제

```sql
SELECT MOD(10, 3);

┌───┐
│ 1  │
└───┘
```
