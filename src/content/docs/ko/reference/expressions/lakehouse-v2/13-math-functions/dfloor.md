---
title: DFLOOR (Lakehouse v2)
description: DFLOOR — `FLOOR`의 별칭입니다. [FLOOR](../floor/)를 참조하십시오.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dfloor.md
---

`FLOOR`의 별칭입니다. [FLOOR](../floor/)를 참조하십시오.

## Analyze 구문

```python
func.dfloor(3.7)
```

## Analyze 예제

```python
func.dfloor(3.7)

┌───┐
│ 3 │
└───┘
```

## SQL 구문

```sql
DFLOOR(<x>)
```

## SQL 예제

```sql
SELECT DFLOOR(3.7);

┌───┐
│ 3 │
└───┘
```
