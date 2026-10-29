---
title: DATE_TRUNC (Lakehouse v2)
description: DATE_TRUNC — trunca un valor de fecha o de fecha y hora a la precisión especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-trunc.md
---

Trunca un valor de fecha o de fecha y hora a la precisión especificada.

## Sintaxis de Analyze

```python
func.date_trunc(<unit>, <datetime>)
```

## Ejemplos de Analyze

```python
func.date_trunc('MONTH', '2024-06-15')

┌──────────────┐
│ '2024-06-01'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
DATE_TRUNC(<unit>, <datetime>)
```

## Ejemplos de SQL

```sql
SELECT DATE_TRUNC('MONTH', '2024-06-15');

┌────────────┐
│ 2024-06-01  │
└────────────┘
```
