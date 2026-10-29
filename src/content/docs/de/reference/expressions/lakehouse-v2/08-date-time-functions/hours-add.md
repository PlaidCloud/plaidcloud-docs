---
title: HOURS_ADD (Lakehouse v2)
description: HOURS_ADD – addiert eine angegebene Anzahl von Stunden zu einem Datums-/Zeitwert.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hours-add.md
---

Addiert eine angegebene Anzahl von Stunden zu einem Datums-/Zeitwert.

## Analyze-Syntax

```python
func.hours_add(<datetime>, <n>)
```

## Analyze-Beispiele

```python
func.hours_add('2024-01-01 10:00:00', 5)

┌───────────────────────┐
│ '2024-01-01 15:00:00'  │
└───────────────────────┘
```

## SQL-Syntax

```sql
HOURS_ADD(<datetime>, <n>)
```

## SQL-Beispiele

```sql
SELECT HOURS_ADD('2024-01-01 10:00:00', 5);

┌─────────────────────┐
│ 2024-01-01 15:00:00  │
└─────────────────────┘
```
