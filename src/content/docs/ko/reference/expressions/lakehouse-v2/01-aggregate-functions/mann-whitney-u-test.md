---
title: MANN_WHITNEY_U_TEST (Lakehouse v2)
description: MANN_WHITNEY_U_TEST — 두 독립 표본에 대해 Mann-Whitney U 검정을 수행합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/mann-whitney-u-test.md
---

두 독립 표본에 대해 Mann-Whitney U 검정을 수행합니다.

## Analyze 구문

```python
func.mann_whitney_u_test(get_column(table, 'sample'), get_column(table, 'treatment'))
```

## Analyze 예제

```python
func.mann_whitney_u_test(get_column(table, 'score'), get_column(table, 'group_id'))

┌─────────────────────────────┐
│ {"U":245.0,"p-value":0.032} │
└─────────────────────────────┘
```

## SQL 구문

```sql
MANN_WHITNEY_U_TEST(<sample>, <treatment>)
```

## SQL 예제

```sql
SELECT MANN_WHITNEY_U_TEST(score, group_id) FROM experiment;

┌─────────────────────────────┐
│ {"U":245.0,"p-value":0.032} │
└─────────────────────────────┘
```
