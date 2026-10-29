---
title: IFNULL (Lakehouse v2)
description: IFNULL — renvoie la première expression si elle n'est pas NULL, sinon renvoie la seconde expression.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/ifnull.md
---

Renvoie la première expression si elle n'est pas NULL, sinon renvoie la seconde expression.

## Syntaxe Analyze

```python
func.ifnull(get_column(table, 'phone'), 'N/A')
```

## Exemples Analyze

```python
func.ifnull(get_column(table, 'phone'), 'N/A')
```

## Syntaxe SQL

```sql
IFNULL(<phone>, 'N/A')
```

## Exemples SQL

```sql
SELECT name, IFNULL(phone, 'N/A') AS phone FROM contacts;

┌─────────┬──────────┐
│ name    │ phone    │
├─────────┼──────────┤
│ Alice   │ 555-1234 │
│ Bob     │ N/A      │
└─────────┴──────────┘
```
