---
title: VAR_SAMP (Lakehouse v2)
description: VAR_SAMP — 표본분산을 반환합니다. `VARIANCE_SAMP`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/var-samp.md
---

표본분산을 반환합니다. `VARIANCE_SAMP`의 별칭입니다.

## Analyze 구문

```python
func.var_samp(get_column(table, 'score'))
```

## Analyze 예제

```python
func.var_samp(get_column(table, 'score'))

┌────────┐
│ 252.48 │
└────────┘
```

## SQL 구문

```sql
VAR_SAMP(<score>)
```

## SQL 예제

```sql
SELECT VAR_SAMP(score) FROM test_results;

┌────────┐
│ 252.48 │
└────────┘
```
