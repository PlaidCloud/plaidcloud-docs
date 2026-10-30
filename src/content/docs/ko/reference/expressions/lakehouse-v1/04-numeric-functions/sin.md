---
title: SIN (Lakehouse v1)
description: SIN — x의 사인을 반환합니다. 이때 x는 라디안 단위입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sin.md
---

`x`의 사인을 반환합니다. 이때 `x`는 라디안 단위입니다.

## Analyze 구문

```python
func.sin( <x> )
```

## Analyze 예시

```python
func.sin(90)

┌────────────────────┐
│    func.sin(90)    │
├────────────────────┤
│ 0.8939966636005579 │
└────────────────────┘
```

## SQL 구문

```sql
SIN( <x> )
```

## SQL 예시

```sql
SELECT SIN(90);

┌────────────────────┐
│       sin(90)      │
├────────────────────┤
│ 0.8939966636005579 │
└────────────────────┘
```
