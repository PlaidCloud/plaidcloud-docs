---
title: TIMEZONE (Lakehouse v1)
description: TIMEZONE – gibt die Zeitzone der aktuellen Verbindung zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/timezone.md
---

Gibt die Zeitzone der aktuellen Verbindung zurück. 

PlaidCloud Lakehouse verwendet standardmäßig UTC (koordinierte Weltzeit) als Zeitzone und erlaubt es Ihnen, die Zeitzone auf Ihren aktuellen geografischen Standort umzustellen. Die verfügbaren Werte für die Einstellung `timezone` finden Sie unter https://docs.rs/chrono-tz/latest/chrono_tz/enum.Tz.html. Details zeigen die folgenden Beispiele.

## Analyze-Syntax

```python
func.timezone()
```

## Analyze-Beispiele

```python
func.timezone()
┌─────────────────────┐
│ timezone            │
├─────────────────────┤
│ UTC                 │
└─────────────────────┘
```

## SQL-Syntax

```sql
SELECT TIMEZONE();
```

## SQL-Beispiele

```sql
-- Return the current timezone
SELECT TIMEZONE();
┌─────────────────┐
│ TIMEZONE('UTC') │
├─────────────────┤
│ UTC             │
└─────────────────┘

-- Set the timezone to China Standard Time
SET timezone='Asia/Shanghai';

SELECT TIMEZONE();
┌───────────────────────────┐
│ TIMEZONE('Asia/Shanghai') │
├───────────────────────────┤
│ Asia/Shanghai             │
└───────────────────────────┘
```
