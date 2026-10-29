---
title: STD (Lakehouse v2)
description: STD — 모표준편차를 반환합니다. `STDDEV_POP`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/std.md
---

모표준편차를 반환합니다. `STDDEV_POP`의 별칭입니다.

## Analyze 구문

```python
func.std(get_column(table, 'score'))
```

## Analyze 예제

```python
func.std(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## SQL 구문

```sql
STD(<score>)
```

## SQL 예제

```sql
SELECT STD(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
