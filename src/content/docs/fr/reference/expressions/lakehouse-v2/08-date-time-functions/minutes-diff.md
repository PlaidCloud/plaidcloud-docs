---
title: MINUTES_DIFF (Lakehouse v2)
description: MINUTES_DIFF — renvoie le nombre de minutes entre deux date-heures.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-diff.md
---

Renvoie le nombre de minutes entre deux date-heures.

## Syntaxe Analyze

```python
func.minutes_diff(<end>, <start>)
```

## Exemples Analyze

```python
func.minutes_diff('2024-01-01 11:00:00', '2024-01-01 10:00:00')

┌────┐
│ 60  │
└────┘
```

## Syntaxe SQL

```sql
MINUTES_DIFF(<end>, <start>)
```

## Exemples SQL

```sql
SELECT MINUTES_DIFF('2024-01-01 11:00:00', '2024-01-01 10:00:00');

┌────┐
│ 60  │
└────┘
```
