---
title: POW (Lakehouse v1)
description: POW — x의 y제곱 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/pow.md
---

`x`의 `y`제곱 값을 반환합니다. 

## Analyze 구문

```python
func.pow( <x, y> )
```

## Analyze 예시

```python
func.pow(-2, 2)

┌────────────────────┐
│ func.pow((- 2), 2) │
├────────────────────┤
│                  4 │ 
└────────────────────┘
```

## SQL 구문

```sql
POW( <x, y> )
```

## 별칭

- [POWER](../power)

## SQL 예시

```sql
SELECT POW(-2, 2), POWER(-2, 2);

┌─────────────────────────────────┐
│ pow((- 2), 2) │ power((- 2), 2) │
├───────────────┼─────────────────┤
│             4 │               4 │
└─────────────────────────────────┘
```
