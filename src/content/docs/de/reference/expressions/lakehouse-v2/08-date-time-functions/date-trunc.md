---
title: DATE_TRUNC (Lakehouse v2)
description: DATE_TRUNC – kürzt einen Datums- oder Datums-/Zeitwert auf die angegebene Genauigkeit.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-trunc.md
---

Kürzt einen Datums- oder Datums-/Zeitwert auf die angegebene Genauigkeit.

## Analyze-Syntax

```python
func.date_trunc(<unit>, <datetime>)
```

## Analyze-Beispiele

```python
func.date_trunc('MONTH', '2024-06-15')

┌──────────────┐
│ '2024-06-01'  │
└──────────────┘
```

## SQL-Syntax

```sql
DATE_TRUNC(<unit>, <datetime>)
```

## SQL-Beispiele

```sql
SELECT DATE_TRUNC('MONTH', '2024-06-15');

┌────────────┐
│ 2024-06-01  │
└────────────┘
```
