---
title: CURRENT_TIMEZONE (Lakehouse v2)
description: CURRENT_TIMEZONE – gibt die aktuelle Zeitzone der Sitzung zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-timezone.md
---

Gibt die aktuelle Zeitzone der Sitzung zurück.

## Analyze-Syntax

```python
func.current_timezone()
```

## Analyze-Beispiele

```python
func.current_timezone()

┌────────────────────┐
│ 'America/New_York'  │
└────────────────────┘
```

## SQL-Syntax

```sql
CURRENT_TIMEZONE()
```

## SQL-Beispiele

```sql
SELECT CURRENT_TIMEZONE();

┌──────────────────┐
│ America/New_York  │
└──────────────────┘
```
