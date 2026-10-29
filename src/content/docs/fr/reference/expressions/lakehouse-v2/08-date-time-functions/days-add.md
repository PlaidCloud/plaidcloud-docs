---
title: DAYS_ADD (Lakehouse v2)
description: DAYS_ADD — ajoute un nombre de jours donné à une date.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/days-add.md
---

Ajoute un nombre de jours donné à une date.

## Syntaxe Analyze

```python
func.days_add(<date>, <n>)
```

## Exemples Analyze

```python
func.days_add('2024-01-01', 30)

┌──────────────┐
│ '2024-01-31'  │
└──────────────┘
```

## Syntaxe SQL

```sql
DAYS_ADD(<date>, <n>)
```

## Exemples SQL

```sql
SELECT DAYS_ADD('2024-01-01', 30);

┌────────────┐
│ 2024-01-31  │
└────────────┘
```
