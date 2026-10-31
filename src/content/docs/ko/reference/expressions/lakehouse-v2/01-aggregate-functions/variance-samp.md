---
title: VARIANCE_SAMP (Lakehouse v2)
description: VARIANCE_SAMP — 표본분산을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/variance-samp.md
---

표본분산을 반환합니다.

## Analyze 구문

```python
func.variance_samp(get_column(table, 'score'))
```

## Analyze 예제

```python
func.variance_samp(get_column(table, 'score'))

┌────────┐
│ 252.48 │
└────────┘
```

## SQL 구문

```sql
VARIANCE_SAMP(<score>)
```

## SQL 예제

```sql
SELECT VARIANCE_SAMP(score) FROM test_results;

┌────────┐
│ 252.48 │
└────────┘
```
