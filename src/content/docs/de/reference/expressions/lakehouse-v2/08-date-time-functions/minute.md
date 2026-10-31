---
title: MINUTE (Lakehouse v2)
description: MINUTE – gibt die Minute aus einem Datum mit Uhrzeit zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minute.md
---

Gibt die Minute aus einem Datum mit Uhrzeit zurück.

## Analyze-Syntax

```python
func.minute(<datetime>)
```

## Analyze-Beispiele

```python
func.minute('2024-06-15 14:30:00')

┌────┐
│ 30  │
└────┘
```

## SQL-Syntax

```sql
MINUTE(<datetime>)
```

## SQL-Beispiele

```sql
SELECT MINUTE('2024-06-15 14:30:00');

┌────┐
│ 30  │
└────┘
```
