---
title: TIMESTAMPDIFF (Lakehouse v2)
description: TIMESTAMPDIFF — renvoie la différence entre deux date-heures dans l'unité spécifiée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestampdiff.md
---

Renvoie la différence entre deux date-heures dans l'unité spécifiée.

## Syntaxe Analyze

```python
func.timestampdiff(<unit>, <start>, <end>)
```

## Exemples Analyze

```python
func.timestampdiff('DAY', '2024-01-01', '2024-03-01')

┌────┐
│ 60  │
└────┘
```

## Syntaxe SQL

```sql
TIMESTAMPDIFF(<unit>, <start>, <end>)
```

## Exemples SQL

```sql
SELECT TIMESTAMPDIFF(DAY, '2024-01-01', '2024-03-01');

┌────┐
│ 60  │
└────┘
```
