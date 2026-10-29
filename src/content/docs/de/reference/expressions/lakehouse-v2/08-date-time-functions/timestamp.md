---
title: TIMESTAMP (Lakehouse v2)
description: TIMESTAMP – wandelt ein Datum oder eine Zeichenfolge in ein Datum mit Uhrzeit um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestamp.md
---

Wandelt ein Datum oder eine Zeichenfolge in ein Datum mit Uhrzeit um.

## Analyze-Syntax

```python
func.timestamp(<expr>)
```

## Analyze-Beispiele

```python
func.timestamp('2024-06-15')

┌───────────────────────┐
│ '2024-06-15 00:00:00'  │
└───────────────────────┘
```

## SQL-Syntax

```sql
TIMESTAMP(<expr>)
```

## SQL-Beispiele

```sql
SELECT TIMESTAMP('2024-06-15');

┌─────────────────────┐
│ 2024-06-15 00:00:00  │
└─────────────────────┘
```
