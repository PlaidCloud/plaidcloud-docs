---
title: TO_TERA_DATE (Lakehouse v2)
description: TO_TERA_DATE — convierte un valor VARCHAR en un valor DATE según una cadena de formato de Teradata.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-tera-date.md
---

Convierte un valor VARCHAR en un valor DATE según una cadena de formato de Teradata.

## Sintaxis de Analyze

```python
func.to_tera_date(<str>, <format>)
```

## Ejemplos de Analyze

```python
func.to_tera_date('20240615', 'YYYYMMDD')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
TO_TERA_DATE(<str>, <format>)
```

## Ejemplos de SQL

```sql
SELECT TO_TERA_DATE('20240615', 'YYYYMMDD');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
