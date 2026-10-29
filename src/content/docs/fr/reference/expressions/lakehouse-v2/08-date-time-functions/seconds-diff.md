---
title: SECONDS_DIFF (Lakehouse v2)
description: SECONDS_DIFF — renvoie le nombre de secondes entre deux date-heures.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-diff.md
---

Renvoie le nombre de secondes entre deux date-heures.

## Syntaxe Analyze

```python
func.seconds_diff(<end>, <start>)
```

## Exemples Analyze

```python
func.seconds_diff('2024-01-01 00:01:30', '2024-01-01 00:00:00')

┌────┐
│ 90  │
└────┘
```

## Syntaxe SQL

```sql
SECONDS_DIFF(<end>, <start>)
```

## Exemples SQL

```sql
SELECT SECONDS_DIFF('2024-01-01 00:01:30', '2024-01-01 00:00:00');

┌────┐
│ 90  │
└────┘
```
