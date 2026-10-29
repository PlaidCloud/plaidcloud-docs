---
title: WEEKS_ADD (Lakehouse v2)
description: WEEKS_ADD – addiert eine angegebene Anzahl von Wochen zu einem Datum.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weeks-add.md
---

Addiert eine angegebene Anzahl von Wochen zu einem Datum.

## Analyze-Syntax

```python
func.weeks_add(<date>, <n>)
```

## Analyze-Beispiele

```python
func.weeks_add('2024-01-01', 2)

┌──────────────┐
│ '2024-01-15'  │
└──────────────┘
```

## SQL-Syntax

```sql
WEEKS_ADD(<date>, <n>)
```

## SQL-Beispiele

```sql
SELECT WEEKS_ADD('2024-01-01', 2);

┌────────────┐
│ 2024-01-15  │
└────────────┘
```
