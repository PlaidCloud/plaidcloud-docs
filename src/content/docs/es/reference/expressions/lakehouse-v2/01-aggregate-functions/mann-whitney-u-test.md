---
title: MANN_WHITNEY_U_TEST (Lakehouse v2)
description: MANN_WHITNEY_U_TEST — realiza una prueba U de Mann-Whitney sobre dos muestras independientes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/mann-whitney-u-test.md
---

Realiza una prueba U de Mann-Whitney sobre dos muestras independientes.

## Sintaxis de Analyze

```python
func.mann_whitney_u_test(get_column(table, 'sample'), get_column(table, 'treatment'))
```

## Ejemplos de Analyze

```python
func.mann_whitney_u_test(get_column(table, 'score'), get_column(table, 'group_id'))

┌─────────────────────────────┐
│ {"U":245.0,"p-value":0.032} │
└─────────────────────────────┘
```

## Sintaxis de SQL

```sql
MANN_WHITNEY_U_TEST(<sample>, <treatment>)
```

## Ejemplos de SQL

```sql
SELECT MANN_WHITNEY_U_TEST(score, group_id) FROM experiment;

┌─────────────────────────────┐
│ {"U":245.0,"p-value":0.032} │
└─────────────────────────────┘
```
