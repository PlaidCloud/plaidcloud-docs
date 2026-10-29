---
title: IFNULL (Lakehouse v2)
description: IFNULL — retorna a primeira expressão se ela não for NULL; caso contrário, retorna a segunda expressão.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/ifnull.md
---

Retorna a primeira expressão se ela não for NULL; caso contrário, retorna a segunda expressão.

## Sintaxe do Analyze

```python
func.ifnull(get_column(table, 'phone'), 'N/A')
```

## Exemplos do Analyze

```python
func.ifnull(get_column(table, 'phone'), 'N/A')
```

## Sintaxe SQL

```sql
IFNULL(<phone>, 'N/A')
```

## Exemplos SQL

```sql
SELECT name, IFNULL(phone, 'N/A') AS phone FROM contacts;

┌─────────┬──────────┐
│ name    │ phone    │
├─────────┼──────────┤
│ Alice   │ 555-1234 │
│ Bob     │ N/A      │
└─────────┴──────────┘
```
