---
title: COS (Lakehouse v1)
description: COS — x의 코사인을 반환합니다. 이때 x는 라디안 단위입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/cos.md
---

`x`의 코사인을 반환합니다. 이때 `x`는 라디안 단위입니다.

## Analyze 구문

```python
func.cos( <x> )
```

## Analyze 예시

```python
func.cos(func.pi())

┌─────────────────────┐
│ func.cos(func.pi()) │
├─────────────────────┤
│                  -1 │
└─────────────────────┘
```

## SQL 구문

```sql
COS( <x> )
```

## SQL 예시

```sql
SELECT COS(PI());

┌───────────┐
│ cos(pi()) │
├───────────┤
│        -1 │
└───────────┘
```
