---
title: IF (Lakehouse v2)
description: IF — devolve um de dois valores consoante uma condição seja TRUE ou FALSE.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/if.md
---

Devolve um de dois valores consoante uma condição seja TRUE ou FALSE.

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
