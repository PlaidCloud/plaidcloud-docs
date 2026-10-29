---
title: STR2DATE (Lakehouse v2)
description: STR2DATE – wandelt eine Zeichenfolge mithilfe einer Formatzeichenfolge in ein Datum um. Alias für `STR_TO_DATE`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str2date.md
---

Wandelt eine Zeichenfolge mithilfe einer Formatzeichenfolge in ein Datum um. Alias für `STR_TO_DATE`.

## Analyze-Syntax

```python
func.str2date(<str>, <format>)
```

## Analyze-Beispiele

```python
func.str2date('2024/06/15', '%Y/%m/%d')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL-Syntax

```sql
STR2DATE(<str>, <format>)
```

## SQL-Beispiele

```sql
SELECT STR2DATE('2024/06/15', '%Y/%m/%d');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
