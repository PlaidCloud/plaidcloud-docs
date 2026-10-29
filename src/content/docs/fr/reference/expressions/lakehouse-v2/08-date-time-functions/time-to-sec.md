---
title: TIME_TO_SEC (Lakehouse v2)
description: TIME_TO_SEC — convertit une valeur d'heure en secondes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/time-to-sec.md
---

Convertit une valeur d'heure en secondes.

## Syntaxe Analyze

```python
func.time_to_sec(<time>)
```

## Exemples Analyze

```python
func.time_to_sec('01:01:01')

┌──────┐
│ 3661  │
└──────┘
```

## Syntaxe SQL

```sql
TIME_TO_SEC(<time>)
```

## Exemples SQL

```sql
SELECT TIME_TO_SEC('01:01:01');

┌──────┐
│ 3661  │
└──────┘
```
