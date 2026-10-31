---
title: TIME_FORMAT (Lakehouse v2)
description: TIME_FORMAT — met en forme une valeur d'heure selon une chaîne de format.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/time-format.md
---

Met en forme une valeur d'heure selon une chaîne de format.

## Syntaxe Analyze

```python
func.time_format(<time>, <format>)
```

## Exemples Analyze

```python
func.time_format('14:30:00', '%H hours %i minutes')

┌───────────────────────┐
│ '14 hours 30 minutes'  │
└───────────────────────┘
```

## Syntaxe SQL

```sql
TIME_FORMAT(<time>, <format>)
```

## Exemples SQL

```sql
SELECT TIME_FORMAT('14:30:00', '%H hours %i minutes');

┌─────────────────────┐
│ 14 hours 30 minutes  │
└─────────────────────┘
```
