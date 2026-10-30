---
title: MINUTES_ADD (Lakehouse v2)
description: MINUTES_ADD — ajoute un nombre donné de minutes à une date-heure.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-add.md
---

Ajoute un nombre donné de minutes à une date-heure.

## Syntaxe Analyze

```python
func.minutes_add(<datetime>, <n>)
```

## Exemples Analyze

```python
func.minutes_add('2024-01-01 10:00:00', 45)

┌───────────────────────┐
│ '2024-01-01 10:45:00'  │
└───────────────────────┘
```

## Syntaxe SQL

```sql
MINUTES_ADD(<datetime>, <n>)
```

## Exemples SQL

```sql
SELECT MINUTES_ADD('2024-01-01 10:00:00', 45);

┌─────────────────────┐
│ 2024-01-01 10:45:00  │
└─────────────────────┘
```
