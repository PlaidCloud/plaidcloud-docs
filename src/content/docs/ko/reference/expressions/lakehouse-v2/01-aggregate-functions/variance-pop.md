---
title: VARIANCE_POP (Lakehouse v2)
description: VARIANCE_POP — 모분산을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/variance-pop.md
---

모분산을 반환합니다.

## Analyze 구문

```python
func.variance_pop(get_column(table, 'score'))
```

## Analyze 예제

```python
func.variance_pop(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## SQL 구문

```sql
VARIANCE_POP(<score>)
```

## SQL 예제

```sql
SELECT VARIANCE_POP(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
