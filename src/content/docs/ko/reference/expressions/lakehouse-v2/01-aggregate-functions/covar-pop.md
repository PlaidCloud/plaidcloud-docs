---
title: COVAR_POP (Lakehouse v2)
description: COVAR_POP — 두 식의 모공분산을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/covar-pop.md
---

두 식의 모공분산을 반환합니다.

## Analyze 구문

```python
func.covar_pop(get_column(table, 'y'), get_column(table, 'x'))
```

## Analyze 예제

```python
func.covar_pop(get_column(table, 'height'), get_column(table, 'weight'))

┌────────┐
│ 102.46 │
└────────┘
```

## SQL 구문

```sql
COVAR_POP(<y>, <x>)
```

## SQL 예제

```sql
SELECT COVAR_POP(height, weight) FROM measurements;

┌────────┐
│ 102.46 │
└────────┘
```
