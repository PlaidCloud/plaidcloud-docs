---
title: LOCALTIMESTAMP (Lakehouse v2)
description: LOCALTIMESTAMP – gibt das aktuelle Datum und die aktuelle Uhrzeit zurück. Alias für `NOW`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/localtimestamp.md
---

Gibt das aktuelle Datum und die aktuelle Uhrzeit zurück. Alias für `NOW`.

## Analyze-Syntax

```python
func.localtimestamp()
```

## Analyze-Beispiele

```python
func.localtimestamp()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQL-Syntax

```sql
LOCALTIMESTAMP()
```

## SQL-Beispiele

```sql
SELECT LOCALTIMESTAMP();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
