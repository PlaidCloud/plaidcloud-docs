---
title: STR_TO_DATE (Lakehouse v2)
description: STR_TO_DATE – wandelt eine Zeichenfolge mithilfe einer Formatzeichenfolge in ein Datum um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str-to-date.md
---

Wandelt eine Zeichenfolge mithilfe einer Formatzeichenfolge in ein Datum um.

## Analyze-Syntax

```python
func.str_to_date(<str>, <format>)
```

## Analyze-Beispiele

```python
func.str_to_date('Jun 15 2024', '%b %d %Y')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL-Syntax

```sql
STR_TO_DATE(<str>, <format>)
```

## SQL-Beispiele

```sql
SELECT STR_TO_DATE('Jun 15 2024', '%b %d %Y');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
