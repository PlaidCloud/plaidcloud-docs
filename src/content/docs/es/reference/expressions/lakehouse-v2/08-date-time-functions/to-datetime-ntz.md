---
title: TO_DATETIME_NTZ (Lakehouse v2)
description: TO_DATETIME_NTZ — convierte un valor en un DATETIME sin zona horaria (NTZ).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-datetime-ntz.md
---

Convierte un valor en un DATETIME sin zona horaria (NTZ). El resultado no se ve afectado por la configuración de zona horaria de la sesión.

## Sintaxis de Analyze

```python
func.to_datetime_ntz('2024-06-15 14:30:00')
```

## Ejemplos de Analyze

```python
func.to_datetime_ntz('2024-06-15 14:30:00')

┌─────────────────────┐
│ 2024-06-15 14:30:00 │
└─────────────────────┘
```

## Sintaxis de SQL

```sql
TO_DATETIME_NTZ(<expr>)
```

## Ejemplos de SQL

```sql
SELECT TO_DATETIME_NTZ('2024-06-15 14:30:00');

┌─────────────────────┐
│ 2024-06-15 14:30:00 │
└─────────────────────┘
```
