---
title: SECOND (Lakehouse v2)
description: SECOND – gibt die Sekunde aus einem Datum mit Uhrzeit zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/second.md
---

Gibt die Sekunde aus einem Datum mit Uhrzeit zurück.

## Analyze-Syntax

```python
func.second(<datetime>)
```

## Analyze-Beispiele

```python
func.second('2024-06-15 14:30:45')

┌────┐
│ 45  │
└────┘
```

## SQL-Syntax

```sql
SECOND(<datetime>)
```

## SQL-Beispiele

```sql
SELECT SECOND('2024-06-15 14:30:45');

┌────┐
│ 45  │
└────┘
```
