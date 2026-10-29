---
title: UTC_TIMESTAMP (Lakehouse v2)
description: UTC_TIMESTAMP – gibt das aktuelle UTC-Datum und die aktuelle UTC-Uhrzeit zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/utc-timestamp.md
---

Gibt das aktuelle UTC-Datum und die aktuelle UTC-Uhrzeit zurück.

## Analyze-Syntax

```python
func.utc_timestamp()
```

## Analyze-Beispiele

```python
func.utc_timestamp()

┌───────────────────────┐
│ '2024-06-15 18:30:00'  │
└───────────────────────┘
```

## SQL-Syntax

```sql
UTC_TIMESTAMP()
```

## SQL-Beispiele

```sql
SELECT UTC_TIMESTAMP();

┌─────────────────────┐
│ 2024-06-15 18:30:00  │
└─────────────────────┘
```
