---
title: STDDEV_SAMP (Lakehouse v2)
description: STDDEV_SAMP — 표본표준편차를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/stddev-samp.md
---

표본표준편차를 반환합니다.

## Analyze 구문

```python
func.stddev_samp(get_column(table, 'score'))
```

## Analyze 예제

```python
func.stddev_samp(get_column(table, 'score'))

┌───────┐
│ 15.89 │
└───────┘
```

## SQL 구문

```sql
STDDEV_SAMP(<score>)
```

## SQL 예제

```sql
SELECT STDDEV_SAMP(score) FROM test_results;

┌───────┐
│ 15.89 │
└───────┘
```
