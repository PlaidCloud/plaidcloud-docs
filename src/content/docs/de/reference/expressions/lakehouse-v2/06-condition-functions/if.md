---
title: IF (Lakehouse v2)
description: IF – gibt je nachdem, ob eine Bedingung TRUE oder FALSE ist, einen von zwei Werten zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/if.md
---

Gibt je nachdem, ob eine Bedingung TRUE oder FALSE ist, einen von zwei Werten zurück.

## Analyze-Syntax

```python
func.if_(get_column(table, 'score') >= 60, 'Pass', 'Fail')
```

## Analyze-Beispiele

```python
func.if_(get_column(table, 'score') >= 60, 'Pass', 'Fail')
```

## SQL-Syntax

```sql
IF(<score> >= 60, 'Pass', 'Fail')
```

## SQL-Beispiele

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
