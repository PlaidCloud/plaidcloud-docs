---
title: CURDATE (Lakehouse v2)
description: CURDATE — renvoie la date du jour.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/curdate.md
---

Renvoie la date du jour.

## Syntaxe Analyze

```python
func.curdate()
```

## Exemples Analyze

```python
func.curdate()

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Syntaxe SQL

```sql
CURDATE()
```

## Exemples SQL

```sql
SELECT CURDATE();

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
