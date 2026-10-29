---
title: CURRENT_DATE (Lakehouse v2)
description: CURRENT_DATE — renvoie la date du jour. Alias de `CURDATE`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-date.md
---

Renvoie la date du jour. Alias de `CURDATE`.

## Syntaxe Analyze

```python
func.current_date()
```

## Exemples Analyze

```python
func.current_date()

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Syntaxe SQL

```sql
CURRENT_DATE()
```

## Exemples SQL

```sql
SELECT CURRENT_DATE();

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
