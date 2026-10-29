---
title: ADD_MONTHS (Lakehouse v2)
description: ADD_MONTHS — ajoute un nombre de mois donné à une date.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/add-months.md
---

Ajoute un nombre de mois donné à une date.

## Syntaxe Analyze

```python
func.add_months(<date>, <months>)
```

## Exemples Analyze

```python
func.add_months('2024-01-31', 1)

┌──────────────┐
│ '2024-02-29'  │
└──────────────┘
```

## Syntaxe SQL

```sql
ADD_MONTHS(<date>, <months>)
```

## Exemples SQL

```sql
SELECT ADD_MONTHS('2024-01-31', 1);

┌────────────┐
│ 2024-02-29  │
└────────────┘
```
