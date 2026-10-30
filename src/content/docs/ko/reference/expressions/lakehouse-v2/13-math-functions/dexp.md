---
title: DEXP (Lakehouse v2)
description: DEXP — `EXP`의 별칭입니다. [EXP](../exp/)를 참조하십시오.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dexp.md
---

`EXP`의 별칭입니다. [EXP](../exp/)를 참조하십시오.

## Analyze 구문

```python
func.dexp(1)
```

## Analyze 예제

```python
func.dexp(1)

┌───────────────────┐
│ 2.718281828459045 │
└───────────────────┘
```

## SQL 구문

```sql
DEXP(<x>)
```

## SQL 예제

```sql
SELECT DEXP(1);

┌───────────────────┐
│ 2.718281828459045 │
└───────────────────┘
```
