---
title: NOW (Lakehouse v2)
description: NOW – gibt das aktuelle Datum und die aktuelle Uhrzeit zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/now.md
---

Gibt das aktuelle Datum und die aktuelle Uhrzeit zurück.

## Analyze-Syntax

```python
func.now()
```

## Analyze-Beispiele

```python
func.now()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQL-Syntax

```sql
NOW()
```

## SQL-Beispiele

```sql
SELECT NOW();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
