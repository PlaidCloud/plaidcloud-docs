---
title: JODATIME_FORMAT (Lakehouse v2)
description: JODATIME_FORMAT – formatiert ein Datum oder einen Datums-/Zeitwert mit Joda-Time-Formatmustern.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/jodatime-format.md
---

Formatiert ein Datum oder einen Datums-/Zeitwert mit Joda-Time-Formatmustern.

## Analyze-Syntax

```python
func.jodatime_format(<datetime>, <pattern>)
```

## Analyze-Beispiele

```python
func.jodatime_format('2024-06-15', 'yyyy/MM/dd')

┌──────────────┐
│ '2024/06/15'  │
└──────────────┘
```

## SQL-Syntax

```sql
JODATIME_FORMAT(<datetime>, <pattern>)
```

## SQL-Beispiele

```sql
SELECT JODATIME_FORMAT('2024-06-15', 'yyyy/MM/dd');

┌────────────┐
│ 2024/06/15  │
└────────────┘
```
