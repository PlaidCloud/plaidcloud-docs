---
title: HOURS_SUB (Lakehouse v2)
description: HOURS_SUB — soustrait un nombre d'heures donné d'une date-heure.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hours-sub.md
---

Soustrait un nombre d'heures donné d'une date-heure.

## Syntaxe Analyze

```python
func.hours_sub(<datetime>, <n>)
```

## Exemples Analyze

```python
func.hours_sub('2024-01-01 15:00:00', 5)

┌───────────────────────┐
│ '2024-01-01 10:00:00'  │
└───────────────────────┘
```

## Syntaxe SQL

```sql
HOURS_SUB(<datetime>, <n>)
```

## Exemples SQL

```sql
SELECT HOURS_SUB('2024-01-01 15:00:00', 5);

┌─────────────────────┐
│ 2024-01-01 10:00:00  │
└─────────────────────┘
```
