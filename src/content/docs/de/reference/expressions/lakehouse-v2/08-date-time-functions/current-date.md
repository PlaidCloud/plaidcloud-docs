---
title: CURRENT_DATE (Lakehouse v2)
description: CURRENT_DATE – gibt das aktuelle Datum zurück. Alias für `CURDATE`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-date.md
---

Gibt das aktuelle Datum zurück. Alias für `CURDATE`.

## Analyze-Syntax

```python
func.current_date()
```

## Analyze-Beispiele

```python
func.current_date()

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL-Syntax

```sql
CURRENT_DATE()
```

## SQL-Beispiele

```sql
SELECT CURRENT_DATE();

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
