---
title: MINUTE (Lakehouse v2)
description: MINUTE — renvoie la minute d'une date-heure.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minute.md
---

Renvoie la minute d'une date-heure.

## Syntaxe Analyze

```python
func.minute(<datetime>)
```

## Exemples Analyze

```python
func.minute('2024-06-15 14:30:00')

┌────┐
│ 30  │
└────┘
```

## Syntaxe SQL

```sql
MINUTE(<datetime>)
```

## Exemples SQL

```sql
SELECT MINUTE('2024-06-15 14:30:00');

┌────┐
│ 30  │
└────┘
```
