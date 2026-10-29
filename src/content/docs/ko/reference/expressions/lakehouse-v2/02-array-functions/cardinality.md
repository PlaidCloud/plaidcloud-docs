---
title: "CARDINALITY (Array, Lakehouse v2)"
description: CARDINALITY — 배열의 요소 수를 반환합니다. `ARRAY_LENGTH`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/cardinality.md
---

배열의 요소 수를 반환합니다. `ARRAY_LENGTH`의 별칭입니다.

## Analyze 구문

```python
func.cardinality([1, 2, 3])
```

## Analyze 예제

```python
func.cardinality([10, 20, 30])

┌───┐
│ 3 │
└───┘
```

## SQL 구문

```sql
CARDINALITY([1, 2, 3])
```

## SQL 예제

```sql
SELECT CARDINALITY([10, 20, 30]);

┌───┐
│ 3 │
└───┘
```
