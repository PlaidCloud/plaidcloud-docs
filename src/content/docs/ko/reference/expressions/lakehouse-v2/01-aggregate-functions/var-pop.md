---
title: VAR_POP (Lakehouse v2)
description: VAR_POP — 모분산을 반환합니다. `VARIANCE_POP`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/var-pop.md
---

모분산을 반환합니다. `VARIANCE_POP`의 별칭입니다.

## Analyze 구문

```python
func.var_pop(get_column(table, 'score'))
```

## Analyze 예제

```python
func.var_pop(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## SQL 구문

```sql
VAR_POP(<score>)
```

## SQL 예제

```sql
SELECT VAR_POP(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
