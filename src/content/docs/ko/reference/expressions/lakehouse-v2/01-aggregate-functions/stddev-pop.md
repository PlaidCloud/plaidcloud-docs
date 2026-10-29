---
title: STDDEV_POP (Lakehouse v2)
description: STDDEV_POP — 모표준편차를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/stddev-pop.md
---

모표준편차를 반환합니다.

## Analyze 구문

```python
func.stddev_pop(get_column(table, 'score'))
```

## Analyze 예제

```python
func.stddev_pop(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## SQL 구문

```sql
STDDEV_POP(<score>)
```

## SQL 예제

```sql
SELECT STDDEV_POP(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
