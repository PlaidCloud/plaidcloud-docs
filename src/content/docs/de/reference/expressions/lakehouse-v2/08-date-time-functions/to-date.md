---
title: TO_DATE (Lakehouse v2)
description: TO_DATE – wandelt ein Datum mit Uhrzeit in ein Datum um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-date.md
---

Wandelt ein Datum mit Uhrzeit in ein Datum um.

## Analyze-Syntax

```python
func.to_date(<datetime>)
```

## Analyze-Beispiele

```python
func.to_date('2024-06-15 14:30:00')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL-Syntax

```sql
TO_DATE(<datetime>)
```

## SQL-Beispiele

```sql
SELECT TO_DATE('2024-06-15 14:30:00');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
