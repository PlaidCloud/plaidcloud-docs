---
title: IF (Lakehouse v2)
description: IF — devuelve uno de dos valores según si una condición es TRUE o FALSE.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/if.md
---

Devuelve uno de dos valores según si una condición es TRUE o FALSE.

## Sintaxis de Analyze

```python
func.if_(get_column(table, 'score') >= 60, 'Pass', 'Fail')
```

## Ejemplos de Analyze

```python
func.if_(get_column(table, 'score') >= 60, 'Pass', 'Fail')
```

## Sintaxis de SQL

```sql
IF(<score> >= 60, 'Pass', 'Fail')
```

## Ejemplos de SQL

```sql
SELECT name, IF(score >= 60, 'Pass', 'Fail') AS result FROM students;

┌─────────┬────────┐
│ name    │ result │
├─────────┼────────┤
│ Alice   │ Pass   │
│ Bob     │ Fail   │
│ Charlie │ Pass   │
└─────────┴────────┘
```
