---
title: DPOW (Lakehouse v2)
description: DPOW — `POW`의 별칭입니다. [POW](../pow/)를 참조하십시오.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dpow.md
---

`POW`의 별칭입니다. [POW](../pow/)를 참조하십시오.

## Analyze 구문

```python
func.dpow(2, 10)
```

## Analyze 예제

```python
func.dpow(2, 10)

┌────────┐
│ 1024.0 │
└────────┘
```

## SQL 구문

```sql
DPOW(<x>)
```

## SQL 예제

```sql
SELECT DPOW(2, 10);

┌────────┐
│ 1024.0 │
└────────┘
```
