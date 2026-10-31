---
title: CURDATE (Lakehouse v2)
description: CURDATE – gibt das aktuelle Datum zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/curdate.md
---

Gibt das aktuelle Datum zurück.

## Analyze-Syntax

```python
func.curdate()
```

## Analyze-Beispiele

```python
func.curdate()

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL-Syntax

```sql
CURDATE()
```

## SQL-Beispiele

```sql
SELECT CURDATE();

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
