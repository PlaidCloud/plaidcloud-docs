---
title: CURTIME (Lakehouse v2)
description: CURTIME – gibt die aktuelle Uhrzeit zurück. Alias für `CURRENT_TIME`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/curtime.md
---

Gibt die aktuelle Uhrzeit zurück. Alias für `CURRENT_TIME`.

## Analyze-Syntax

```python
func.curtime()
```

## Analyze-Beispiele

```python
func.curtime()

┌────────────┐
│ '14:30:00'  │
└────────────┘
```

## SQL-Syntax

```sql
CURTIME()
```

## SQL-Beispiele

```sql
SELECT CURTIME();

┌──────────┐
│ 14:30:00  │
└──────────┘
```
