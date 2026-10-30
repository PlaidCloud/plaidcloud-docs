---
title: COVAR_SAMP (Lakehouse v2)
description: COVAR_SAMP — 두 식의 표본공분산을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/covar-samp.md
---

두 식의 표본공분산을 반환합니다.

## Analyze 구문

```python
func.covar_samp(get_column(table, 'y'), get_column(table, 'x'))
```

## Analyze 예제

```python
func.covar_samp(get_column(table, 'height'), get_column(table, 'weight'))

┌────────┐
│ 103.01 │
└────────┘
```

## SQL 구문

```sql
COVAR_SAMP(<y>, <x>)
```

## SQL 예제

```sql
SELECT COVAR_SAMP(height, weight) FROM measurements;

┌────────┐
│ 103.01 │
└────────┘
```
