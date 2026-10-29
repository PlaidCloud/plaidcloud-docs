---
title: HOUR (Lakehouse v2)
description: HOUR — renvoie l'heure d'une date-heure.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hour.md
---

Renvoie l'heure d'une date-heure.

## Syntaxe Analyze

```python
func.hour(<datetime>)
```

## Exemples Analyze

```python
func.hour('2024-06-15 14:30:00')

┌────┐
│ 14  │
└────┘
```

## Syntaxe SQL

```sql
HOUR(<datetime>)
```

## Exemples SQL

```sql
SELECT HOUR('2024-06-15 14:30:00');

┌────┐
│ 14  │
└────┘
```
