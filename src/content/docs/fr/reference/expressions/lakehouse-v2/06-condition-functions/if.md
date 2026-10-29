---
title: IF (Lakehouse v2)
description: IF — renvoie l'une de deux valeurs selon qu'une condition est TRUE ou FALSE.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/if.md
---

Renvoie l'une de deux valeurs selon qu'une condition est TRUE ou FALSE.

## Syntaxe Analyze

```python
func.if_(get_column(table, 'score') >= 60, 'Pass', 'Fail')
```

## Exemples Analyze

```python
func.if_(get_column(table, 'score') >= 60, 'Pass', 'Fail')
```

## Syntaxe SQL

```sql
IF(<score> >= 60, 'Pass', 'Fail')
```

## Exemples SQL

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
