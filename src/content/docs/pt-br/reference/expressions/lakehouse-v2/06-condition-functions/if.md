---
title: IF (Lakehouse v2)
description: IF — retorna um entre dois valores, dependendo de a condição ser TRUE ou FALSE.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/if.md
---

Retorna um entre dois valores, dependendo de a condição ser TRUE ou FALSE.

## Sintaxe do Analyze

```python
func.if_(get_column(table, 'score') >= 60, 'Pass', 'Fail')
```

## Exemplos do Analyze

```python
func.if_(get_column(table, 'score') >= 60, 'Pass', 'Fail')
```

## Sintaxe SQL

```sql
IF(<score> >= 60, 'Pass', 'Fail')
```

## Exemplos SQL

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
