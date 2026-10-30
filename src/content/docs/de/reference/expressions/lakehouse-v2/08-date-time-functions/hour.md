---
title: HOUR (Lakehouse v2)
description: HOUR – gibt die Stunde aus einem Datums-/Zeitwert zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hour.md
---

Gibt die Stunde aus einem Datums-/Zeitwert zurück.

## Analyze-Syntax

```python
func.hour(<datetime>)
```

## Analyze-Beispiele

```python
func.hour('2024-06-15 14:30:00')

┌────┐
│ 14  │
└────┘
```

## SQL-Syntax

```sql
HOUR(<datetime>)
```

## SQL-Beispiele

```sql
SELECT HOUR('2024-06-15 14:30:00');

┌────┐
│ 14  │
└────┘
```
