---
title: SECONDS_SUB (Lakehouse v2)
description: SECONDS_SUB – subtrahiert eine angegebene Anzahl von Sekunden von einem Datum mit Uhrzeit.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-sub.md
---

Subtrahiert eine angegebene Anzahl von Sekunden von einem Datum mit Uhrzeit.

## Analyze-Syntax

```python
func.seconds_sub(<datetime>, <n>)
```

## Analyze-Beispiele

```python
func.seconds_sub('2024-01-01 00:01:30', 90)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## SQL-Syntax

```sql
SECONDS_SUB(<datetime>, <n>)
```

## SQL-Beispiele

```sql
SELECT SECONDS_SUB('2024-01-01 00:01:30', 90);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```
