---
title: TO_TERA_TIMESTAMP (Lakehouse v2)
description: "Use la función de fecha y hora TO_TERA_TIMESTAMP en PlaidCloud Lakehouse. Convierte un valor VARCHAR en un valor DATETIME según una cadena de formato de Teradata."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-tera-timestamp.md
---

Convierte un valor VARCHAR en un valor DATETIME según una cadena de formato de Teradata.

## Sintaxis de Analyze

```python
func.to_tera_timestamp(<str>, <format>)
```

## Ejemplos de Analyze

```python
func.to_tera_timestamp('20240615143000', 'YYYYMMDDHH24MISS')

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
TO_TERA_TIMESTAMP(<str>, <format>)
```

## Ejemplos de SQL

```sql
SELECT TO_TERA_TIMESTAMP('20240615143000', 'YYYYMMDDHH24MISS');

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
