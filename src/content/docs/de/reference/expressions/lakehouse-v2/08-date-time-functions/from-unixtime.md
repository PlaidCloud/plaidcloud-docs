---
title: FROM_UNIXTIME (Lakehouse v2)
description: FROM_UNIXTIME – wandelt einen Unix-Zeitstempel in eine Datums-/Zeitzeichenfolge um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/from-unixtime.md
---

Wandelt einen Unix-Zeitstempel in eine Datums-/Zeitzeichenfolge um.

## Analyze-Syntax

```python
func.from_unixtime(<timestamp>[, <format>])
```

## Analyze-Beispiele

```python
func.from_unixtime(1704067200)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## SQL-Syntax

```sql
FROM_UNIXTIME(<timestamp>[, <format>])
```

## SQL-Beispiele

```sql
SELECT FROM_UNIXTIME(1704067200);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```
