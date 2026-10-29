---
title: HOURS_DIFF (Lakehouse v2)
description: HOURS_DIFF — renvoie le nombre d'heures entre deux date-heure.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hours-diff.md
---

Renvoie le nombre d'heures entre deux date-heure.

## Syntaxe Analyze

```python
func.hours_diff(<end>, <start>)
```

## Exemples Analyze

```python
func.hours_diff('2024-01-02 10:00:00', '2024-01-01 10:00:00')

┌────┐
│ 24  │
└────┘
```

## Syntaxe SQL

```sql
HOURS_DIFF(<end>, <start>)
```

## Exemples SQL

```sql
SELECT HOURS_DIFF('2024-01-02 10:00:00', '2024-01-01 10:00:00');

┌────┐
│ 24  │
└────┘
```
