---
title: TO_DATETIME (Lakehouse v2)
description: TO_DATETIME – wandelt einen Wert in ein Datum mit Uhrzeit um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-datetime.md
---

Wandelt einen Wert in ein Datum mit Uhrzeit um.

## Analyze-Syntax

```python
func.to_datetime(<expr>)
```

## Analyze-Beispiele

```python
func.to_datetime('2024-06-15')

┌───────────────────────┐
│ '2024-06-15 00:00:00'  │
└───────────────────────┘
```

## SQL-Syntax

```sql
TO_DATETIME(<expr>)
```

## SQL-Beispiele

```sql
SELECT TO_DATETIME('2024-06-15');

┌─────────────────────┐
│ 2024-06-15 00:00:00  │
└─────────────────────┘
```
