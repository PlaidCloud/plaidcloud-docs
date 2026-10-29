---
title: PMOD (Lakehouse v2)
description: PMOD — 두 숫자를 나눈 양의 나머지를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/pmod.md
---

두 숫자를 나눈 양의 나머지를 반환합니다.

## Analyze 구문

```python
func.pmod(<x>, <y>)
```

## Analyze 예제

```python
func.pmod(-10, 3)

┌───┐
│ 2  │
└───┘
```

## SQL 구문

```sql
PMOD(<x>, <y>)
```

## SQL 예제

```sql
SELECT PMOD(-10, 3);

┌───┐
│ 2  │
└───┘
```
