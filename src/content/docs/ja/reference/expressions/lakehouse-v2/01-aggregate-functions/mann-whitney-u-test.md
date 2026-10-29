---
title: MANN_WHITNEY_U_TEST (Lakehouse v2)
description: MANN_WHITNEY_U_TEST — 2 つの独立した標本に対してマン・ホイットニーの U 検定を実行します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/mann-whitney-u-test.md
---

2 つの独立した標本に対してマン・ホイットニーの U 検定を実行します。

## Analyzeの構文

```python
func.mann_whitney_u_test(get_column(table, 'sample'), get_column(table, 'treatment'))
```

## Analyzeの例

```python
func.mann_whitney_u_test(get_column(table, 'score'), get_column(table, 'group_id'))

┌─────────────────────────────┐
│ {"U":245.0,"p-value":0.032} │
└─────────────────────────────┘
```

## SQLの構文

```sql
MANN_WHITNEY_U_TEST(<sample>, <treatment>)
```

## SQLの例

```sql
SELECT MANN_WHITNEY_U_TEST(score, group_id) FROM experiment;

┌─────────────────────────────┐
│ {"U":245.0,"p-value":0.032} │
└─────────────────────────────┘
```
