---
title: LOCALTIME (Lakehouse v2)
description: LOCALTIME – gibt das aktuelle Datum und die aktuelle Uhrzeit zurück. Alias für `NOW`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/localtime.md
---

Gibt das aktuelle Datum und die aktuelle Uhrzeit zurück. Alias für `NOW`.

## Analyze-Syntax

```python
func.localtime()
```

## Analyze-Beispiele

```python
func.localtime()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQL-Syntax

```sql
LOCALTIME()
```

## SQL-Beispiele

```sql
SELECT LOCALTIME();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
