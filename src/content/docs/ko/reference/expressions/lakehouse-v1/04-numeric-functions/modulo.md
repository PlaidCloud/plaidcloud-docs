---
title: MODULO (Lakehouse v1)
description: MODULO — x를 y로 나눈 나머지를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/modulo.md
---

`x`를 `y`로 나눈 나머지를 반환합니다. `y`가 0이면 오류를 반환합니다.

## Analyze 구문

```python
func.modulo( <x>, <y> )
```

## Analyze 예시

```python
func.modulo(9, 2)

┌───────────────────┐
│ func.modulo(9, 2) │
├───────────────────┤
│                 1 │
└───────────────────┘
```

## SQL 구문

```sql
MODULO( <x>, <y> )
```

## 별칭

- [MOD](../mod)

## SQL 예시

```sql
SELECT MOD(9, 2), MODULO(9, 2);

┌──────────────────────────┐
│ mod(9, 2) │ modulo(9, 2) │
├───────────┼──────────────┤
│         1 │            1 │
└──────────────────────────┘
```
