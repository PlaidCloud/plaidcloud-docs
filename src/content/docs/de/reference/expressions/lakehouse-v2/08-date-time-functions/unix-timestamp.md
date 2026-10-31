---
title: UNIX_TIMESTAMP (Lakehouse v2)
description: UNIX_TIMESTAMP – wandelt ein Datum mit Uhrzeit in einen Unix-Zeitstempel um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/unix-timestamp.md
---

Wandelt ein Datum mit Uhrzeit in einen Unix-Zeitstempel um.

## Analyze-Syntax

```python
func.unix_timestamp([<datetime>])
```

## Analyze-Beispiele

```python
func.unix_timestamp('2024-01-01 00:00:00')

┌────────────┐
│ 1704067200  │
└────────────┘
```

## SQL-Syntax

```sql
UNIX_TIMESTAMP([<datetime>])
```

## SQL-Beispiele

```sql
SELECT UNIX_TIMESTAMP('2024-01-01 00:00:00');

┌────────────┐
│ 1704067200  │
└────────────┘
```
