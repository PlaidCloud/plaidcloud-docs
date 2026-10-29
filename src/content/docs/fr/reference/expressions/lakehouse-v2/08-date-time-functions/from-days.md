---
title: FROM_DAYS (Lakehouse v2)
description: FROM_DAYS — convertit un nombre de jours en date.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/from-days.md
---

Convertit un nombre de jours en date.

## Syntaxe Analyze

```python
func.from_days(<n>)
```

## Exemples Analyze

```python
func.from_days(738886)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## Syntaxe SQL

```sql
FROM_DAYS(<n>)
```

## Exemples SQL

```sql
SELECT FROM_DAYS(738886);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
