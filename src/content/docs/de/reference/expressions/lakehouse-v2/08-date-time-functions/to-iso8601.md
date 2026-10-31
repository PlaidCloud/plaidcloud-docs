---
title: TO_ISO8601 (Lakehouse v2)
description: TO_ISO8601 – wandelt ein Datum oder ein Datum mit Uhrzeit in eine ISO-8601-formatierte Zeichenfolge um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-iso8601.md
---

Wandelt ein Datum oder ein Datum mit Uhrzeit in eine ISO-8601-formatierte Zeichenfolge um.

## Analyze-Syntax

```python
func.to_iso8601(<datetime>)
```

## Analyze-Beispiele

```python
func.to_iso8601('2024-06-15 14:30:00')

┌───────────────────────┐
│ '2024-06-15T14:30:00'  │
└───────────────────────┘
```

## SQL-Syntax

```sql
TO_ISO8601(<datetime>)
```

## SQL-Beispiele

```sql
SELECT TO_ISO8601('2024-06-15 14:30:00');

┌─────────────────────┐
│ 2024-06-15T14:30:00  │
└─────────────────────┘
```
