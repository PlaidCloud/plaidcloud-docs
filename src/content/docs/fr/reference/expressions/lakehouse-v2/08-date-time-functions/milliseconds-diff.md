---
title: MILLISECONDS_DIFF (Lakehouse v2)
description: MILLISECONDS_DIFF — renvoie le nombre de millisecondes entre deux date-heures.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/milliseconds-diff.md
---

Renvoie le nombre de millisecondes entre deux date-heures.

## Syntaxe Analyze

```python
func.milliseconds_diff(<end>, <start>)
```

## Exemples Analyze

```python
func.milliseconds_diff('2024-01-01 00:00:01', '2024-01-01 00:00:00')

┌──────┐
│ 1000  │
└──────┘
```

## Syntaxe SQL

```sql
MILLISECONDS_DIFF(<end>, <start>)
```

## Exemples SQL

```sql
SELECT MILLISECONDS_DIFF('2024-01-01 00:00:01', '2024-01-01 00:00:00');

┌──────┐
│ 1000  │
└──────┘
```
