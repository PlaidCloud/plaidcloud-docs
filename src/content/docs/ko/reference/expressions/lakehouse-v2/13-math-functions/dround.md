---
title: DROUND (Lakehouse v2)
description: DROUND — `ROUND`의 별칭입니다. [ROUND](../round/)를 참조하십시오.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dround.md
---

`ROUND`의 별칭입니다. [ROUND](../round/)를 참조하십시오.

## Analyze 구문

```python
func.dround(3.14159, 2)
```

## Analyze 예제

```python
func.dround(3.14159, 2)

┌──────┐
│ 3.14 │
└──────┘
```

## SQL 구문

```sql
DROUND(<x>)
```

## SQL 예제

```sql
SELECT DROUND(3.14159, 2);

┌──────┐
│ 3.14 │
└──────┘
```
