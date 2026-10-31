---
title: TO_TERA_DATE (Lakehouse v2)
description: TO_TERA_DATE – wandelt einen VARCHAR-Wert gemäß einer Teradata-Formatzeichenfolge in einen DATE-Wert um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-tera-date.md
---

Wandelt einen VARCHAR-Wert gemäß einer Teradata-Formatzeichenfolge in einen DATE-Wert um.

## Analyze-Syntax

```python
func.to_tera_date(<str>, <format>)
```

## Analyze-Beispiele

```python
func.to_tera_date('20240615', 'YYYYMMDD')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL-Syntax

```sql
TO_TERA_DATE(<str>, <format>)
```

## SQL-Beispiele

```sql
SELECT TO_TERA_DATE('20240615', 'YYYYMMDD');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
