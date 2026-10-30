---
title: CONTAINS (Lakehouse v1)
description: CONTAINS — 배열에 특정 요소가 포함되어 있는지 확인합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/contains.md
---

배열에 특정 요소가 포함되어 있는지 확인합니다.


## Analyze 구문

```python
func.contains( <array>, <element> )
```

## Analyze 예제

```python
func.contains([1, 2], 1)

┌───────────────────────────┐
│ func.contains([1, 2], 1)  │
├───────────────────────────┤
│ true                      │
└───────────────────────────┘
```

## SQL 구문

```sql
CONTAINS( <array>, <element> )
```

## 별칭

- [ARRAY_CONTAINS](../array-contains)

## SQL 예제

```sql
SELECT ARRAY_CONTAINS([1, 2], 1), CONTAINS([1, 2], 1);

┌─────────────────────────────────────────────────┐
│ array_contains([1, 2], 1) │ contains([1, 2], 1) │
├───────────────────────────┼─────────────────────┤
│ true                      │ true                │
└─────────────────────────────────────────────────┘
```
