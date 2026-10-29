---
title: ASIN (Lakehouse v1)
description: ASIN — x의 아크사인, 즉 사인 값이 x인 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/asin.md
---

`x`의 아크사인, 즉 사인 값이 `x`인 값을 반환합니다. `x`가 -1에서 1 범위에 없으면 NULL을 반환합니다.

## Analyze 구문

```python
func.asin( <x> )
```

## Analyze 예시

```python
func.asin(0.2)

┌────────────────────┐
│   func.asin(0.2)   │
├────────────────────┤
│ 0.2013579207903308 │
└────────────────────┘
```

## SQL 구문

```sql
ASIN( <x> )
```

## SQL 예시

```sql
SELECT ASIN(0.2);

┌────────────────────┐
│      asin(0.2)     │
├────────────────────┤
│ 0.2013579207903308 │
└────────────────────┘
```
