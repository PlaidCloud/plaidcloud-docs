---
title: STR_TO_DATE (Lakehouse v2)
description: STR_TO_DATE — convierte una cadena en una fecha mediante una cadena de formato.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str-to-date.md
---

Convierte una cadena en una fecha mediante una cadena de formato.

## Sintaxis de Analyze

```python
func.str_to_date(<str>, <format>)
```

## Ejemplos de Analyze

```python
func.str_to_date('Jun 15 2024', '%b %d %Y')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
STR_TO_DATE(<str>, <format>)
```

## Ejemplos de SQL

```sql
SELECT STR_TO_DATE('Jun 15 2024', '%b %d %Y');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
