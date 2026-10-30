---
title: CURRENT_TIMESTAMP (Lakehouse v2)
description: CURRENT_TIMESTAMP – gibt das aktuelle Datum und die aktuelle Uhrzeit zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-timestamp.md
---

Gibt das aktuelle Datum und die aktuelle Uhrzeit zurück.

## Analyze-Syntax

```python
func.current_timestamp()
```

## Analyze-Beispiele

```python
func.current_timestamp()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQL-Syntax

```sql
CURRENT_TIMESTAMP()
```

## SQL-Beispiele

```sql
SELECT CURRENT_TIMESTAMP();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
