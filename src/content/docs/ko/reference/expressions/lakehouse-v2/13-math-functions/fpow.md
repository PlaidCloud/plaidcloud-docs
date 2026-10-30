---
title: FPOW (Lakehouse v2)
description: FPOW — `POW`의 별칭입니다. [POW](../pow/)를 참조하십시오.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/fpow.md
---

`POW`의 별칭입니다. [POW](../pow/)를 참조하십시오.

## Analyze 구문

```python
func.fpow(2, 10)
```

## Analyze 예제

```python
func.fpow(2, 10)

┌────────┐
│ 1024.0 │
└────────┘
```

## SQL 구문

```sql
FPOW(<x>)
```

## SQL 예제

```sql
SELECT FPOW(2, 10);

┌────────┐
│ 1024.0 │
└────────┘
```
