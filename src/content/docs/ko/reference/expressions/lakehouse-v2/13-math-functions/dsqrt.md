---
title: DSQRT (Lakehouse v2)
description: DSQRT — `SQRT`의 별칭입니다. [SQRT](../sqrt/)를 참조하십시오.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dsqrt.md
---

`SQRT`의 별칭입니다. [SQRT](../sqrt/)를 참조하십시오.

## Analyze 구문

```python
func.dsqrt(144)
```

## Analyze 예제

```python
func.dsqrt(144)

┌──────┐
│ 12.0 │
└──────┘
```

## SQL 구문

```sql
DSQRT(<x>)
```

## SQL 예제

```sql
SELECT DSQRT(144);

┌──────┐
│ 12.0 │
└──────┘
```
