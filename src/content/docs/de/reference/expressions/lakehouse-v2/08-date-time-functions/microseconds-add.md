---
title: MICROSECONDS_ADD (Lakehouse v2)
description: MICROSECONDS_ADD – addiert eine angegebene Anzahl von Mikrosekunden zu einem Datum mit Uhrzeit.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/microseconds-add.md
---

Addiert eine angegebene Anzahl von Mikrosekunden zu einem Datum mit Uhrzeit.

## Analyze-Syntax

```python
func.microseconds_add(<datetime>, <n>)
```

## Analyze-Beispiele

```python
func.microseconds_add('2024-01-01 00:00:00', 1000000)

┌───────────────────────┐
│ '2024-01-01 00:00:01'  │
└───────────────────────┘
```

## SQL-Syntax

```sql
MICROSECONDS_ADD(<datetime>, <n>)
```

## SQL-Beispiele

```sql
SELECT MICROSECONDS_ADD('2024-01-01 00:00:00', 1000000);

┌─────────────────────┐
│ 2024-01-01 00:00:01  │
└─────────────────────┘
```
