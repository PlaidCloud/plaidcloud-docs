---
title: VARIANCE (Lakehouse v2)
description: VARIANCE — 모분산을 반환합니다. `VARIANCE_POP`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/variance.md
---

모분산을 반환합니다. `VARIANCE_POP`의 별칭입니다.

## Analyze 구문

```python
func.variance(get_column(table, 'score'))
```

## Analyze 예제

```python
func.variance(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## SQL 구문

```sql
VARIANCE(<score>)
```

## SQL 예제

```sql
SELECT VARIANCE(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
