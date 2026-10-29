---
title: MINUTES_ADD (Lakehouse v2)
description: MINUTES_ADD – addiert eine angegebene Anzahl von Minuten zu einem Datum mit Uhrzeit.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-add.md
---

Addiert eine angegebene Anzahl von Minuten zu einem Datum mit Uhrzeit.

## Analyze-Syntax

```python
func.minutes_add(<datetime>, <n>)
```

## Analyze-Beispiele

```python
func.minutes_add('2024-01-01 10:00:00', 45)

┌───────────────────────┐
│ '2024-01-01 10:45:00'  │
└───────────────────────┘
```

## SQL-Syntax

```sql
MINUTES_ADD(<datetime>, <n>)
```

## SQL-Beispiele

```sql
SELECT MINUTES_ADD('2024-01-01 10:00:00', 45);

┌─────────────────────┐
│ 2024-01-01 10:45:00  │
└─────────────────────┘
```
