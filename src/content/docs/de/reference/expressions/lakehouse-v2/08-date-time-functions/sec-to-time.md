---
title: SEC_TO_TIME (Lakehouse v2)
description: SEC_TO_TIME – wandelt Sekunden in einen Zeitwert um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/sec-to-time.md
---

Wandelt Sekunden in einen Zeitwert um.

## Analyze-Syntax

```python
func.sec_to_time(<seconds>)
```

## Analyze-Beispiele

```python
func.sec_to_time(3661)

┌────────────┐
│ '01:01:01'  │
└────────────┘
```

## SQL-Syntax

```sql
SEC_TO_TIME(<seconds>)
```

## SQL-Beispiele

```sql
SELECT SEC_TO_TIME(3661);

┌──────────┐
│ 01:01:01  │
└──────────┘
```
