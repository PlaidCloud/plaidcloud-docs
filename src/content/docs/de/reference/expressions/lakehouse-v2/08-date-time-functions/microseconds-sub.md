---
title: MICROSECONDS_SUB (Lakehouse v2)
description: MICROSECONDS_SUB – subtrahiert eine angegebene Anzahl von Mikrosekunden von einem Datum mit Uhrzeit.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/microseconds-sub.md
---

Subtrahiert eine angegebene Anzahl von Mikrosekunden von einem Datum mit Uhrzeit.

## Analyze-Syntax

```python
func.microseconds_sub(<datetime>, <n>)
```

## Analyze-Beispiele

```python
func.microseconds_sub('2024-01-01 00:00:01', 1000000)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## SQL-Syntax

```sql
MICROSECONDS_SUB(<datetime>, <n>)
```

## SQL-Beispiele

```sql
SELECT MICROSECONDS_SUB('2024-01-01 00:00:01', 1000000);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```
