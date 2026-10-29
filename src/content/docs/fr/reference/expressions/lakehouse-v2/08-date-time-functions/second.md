---
title: SECOND (Lakehouse v2)
description: SECOND — renvoie la seconde d'une date-heure.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/second.md
---

Renvoie la seconde d'une date-heure.

## Syntaxe Analyze

```python
func.second(<datetime>)
```

## Exemples Analyze

```python
func.second('2024-06-15 14:30:45')

┌────┐
│ 45  │
└────┘
```

## Syntaxe SQL

```sql
SECOND(<datetime>)
```

## Exemples SQL

```sql
SELECT SECOND('2024-06-15 14:30:45');

┌────┐
│ 45  │
└────┘
```
