---
title: ACOS (Lakehouse v1)
description: ACOS — x의 아크코사인, 즉 코사인 값이 x인 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/acos.md
---

`x`의 아크코사인, 즉 코사인 값이 `x`인 값을 반환합니다. `x`가 -1에서 1 범위에 없으면 NULL을 반환합니다.

## Analyze 구문

```python
func.abs( <x> )
```

## Analyze 예시

```python
func.abs(1)

┌──────────────┐
│ func.acos(1) │
├──────────────┤
│            0 │
└──────────────┘
```

## SQL 구문

```sql
ACOS( <x> )
```

## SQL 예시

```sql
SELECT ACOS(1);

┌─────────┐
│ acos(1) │
├─────────┤
│       0 │
└─────────┘
```
