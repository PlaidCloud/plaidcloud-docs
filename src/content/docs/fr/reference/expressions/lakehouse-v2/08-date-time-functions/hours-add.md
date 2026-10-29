---
title: HOURS_ADD (Lakehouse v2)
description: HOURS_ADD — ajoute un nombre d'heures donné à une date-heure.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hours-add.md
---

Ajoute un nombre d'heures donné à une date-heure.

## Syntaxe Analyze

```python
func.hours_add(<datetime>, <n>)
```

## Exemples Analyze

```python
func.hours_add('2024-01-01 10:00:00', 5)

┌───────────────────────┐
│ '2024-01-01 15:00:00'  │
└───────────────────────┘
```

## Syntaxe SQL

```sql
HOURS_ADD(<datetime>, <n>)
```

## Exemples SQL

```sql
SELECT HOURS_ADD('2024-01-01 10:00:00', 5);

┌─────────────────────┐
│ 2024-01-01 15:00:00  │
└─────────────────────┘
```
