---
title: SECONDS_ADD (Lakehouse v2)
description: SECONDS_ADD – addiert eine angegebene Anzahl von Sekunden zu einem Datum mit Uhrzeit.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-add.md
---

Addiert eine angegebene Anzahl von Sekunden zu einem Datum mit Uhrzeit.

## Analyze-Syntax

```python
func.seconds_add(<datetime>, <n>)
```

## Analyze-Beispiele

```python
func.seconds_add('2024-01-01 00:00:00', 90)

┌───────────────────────┐
│ '2024-01-01 00:01:30'  │
└───────────────────────┘
```

## SQL-Syntax

```sql
SECONDS_ADD(<datetime>, <n>)
```

## SQL-Beispiele

```sql
SELECT SECONDS_ADD('2024-01-01 00:00:00', 90);

┌─────────────────────┐
│ 2024-01-01 00:01:30  │
└─────────────────────┘
```
