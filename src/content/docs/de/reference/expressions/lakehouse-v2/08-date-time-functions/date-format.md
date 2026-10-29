---
title: DATE_FORMAT (Lakehouse v2)
description: DATE_FORMAT – formatiert einen Datums- oder Datums-/Zeitwert gemäß einer Formatzeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-format.md
---

Formatiert einen Datums- oder Datums-/Zeitwert gemäß einer Formatzeichenfolge.

## Analyze-Syntax

```python
func.date_format(<date>, <format>)
```

## Analyze-Beispiele

```python
func.date_format('2024-06-15', '%Y/%m/%d')

┌──────────────┐
│ '2024/06/15'  │
└──────────────┘
```

## SQL-Syntax

```sql
DATE_FORMAT(<date>, <format>)
```

## SQL-Beispiele

```sql
SELECT DATE_FORMAT('2024-06-15', '%Y/%m/%d');

┌────────────┐
│ 2024/06/15  │
└────────────┘
```
