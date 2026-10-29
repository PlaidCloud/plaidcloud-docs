---
title: TO_DAYS (Lakehouse v2)
description: TO_DAYS — convertit une date en nombre de jours.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-days.md
---

Convertit une date en nombre de jours.

## Syntaxe Analyze

```python
func.to_days(<date>)
```

## Exemples Analyze

```python
func.to_days('2024-01-01')

┌────────┐
│ 738886  │
└────────┘
```

## Syntaxe SQL

```sql
TO_DAYS(<date>)
```

## Exemples SQL

```sql
SELECT TO_DAYS('2024-01-01');

┌────────┐
│ 738886  │
└────────┘
```
