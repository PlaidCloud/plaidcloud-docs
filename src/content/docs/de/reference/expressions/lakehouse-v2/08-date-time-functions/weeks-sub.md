---
title: WEEKS_SUB (Lakehouse v2)
description: WEEKS_SUB – subtrahiert eine angegebene Anzahl von Wochen von einem Datum.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weeks-sub.md
---

Subtrahiert eine angegebene Anzahl von Wochen von einem Datum.

## Analyze-Syntax

```python
func.weeks_sub(<date>, <n>)
```

## Analyze-Beispiele

```python
func.weeks_sub('2024-01-15', 2)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## SQL-Syntax

```sql
WEEKS_SUB(<date>, <n>)
```

## SQL-Beispiele

```sql
SELECT WEEKS_SUB('2024-01-15', 2);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
