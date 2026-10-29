---
title: TO_DATETIME_NTZ (Lakehouse v2)
description: TO_DATETIME_NTZ – wandelt einen Wert in ein DATETIME ohne Zeitzone (NTZ) um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-datetime-ntz.md
---

Wandelt einen Wert in ein DATETIME ohne Zeitzone (NTZ) um. Das Ergebnis wird von den Zeitzoneneinstellungen der Sitzung nicht beeinflusst.

## Analyze-Syntax

```python
func.to_datetime_ntz('2024-06-15 14:30:00')
```

## Analyze-Beispiele

```python
func.to_datetime_ntz('2024-06-15 14:30:00')

┌─────────────────────┐
│ 2024-06-15 14:30:00 │
└─────────────────────┘
```

## SQL-Syntax

```sql
TO_DATETIME_NTZ(<expr>)
```

## SQL-Beispiele

```sql
SELECT TO_DATETIME_NTZ('2024-06-15 14:30:00');

┌─────────────────────┐
│ 2024-06-15 14:30:00 │
└─────────────────────┘
```
