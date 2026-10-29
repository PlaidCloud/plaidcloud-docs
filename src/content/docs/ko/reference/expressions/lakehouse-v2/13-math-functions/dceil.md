---
title: DCEIL (Lakehouse v2)
description: DCEIL — `CEIL`의 별칭입니다. [CEIL](../ceil/)을 참조하십시오.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dceil.md
---

`CEIL`의 별칭입니다. [CEIL](../ceil/)을 참조하십시오.

## Analyze 구문

```python
func.dceil(3.2)
```

## Analyze 예제

```python
func.dceil(3.2)

┌───┐
│ 4 │
└───┘
```

## SQL 구문

```sql
DCEIL(<x>)
```

## SQL 예제

```sql
SELECT DCEIL(3.2);

┌───┐
│ 4 │
└───┘
```
