---
title: DATE_FORMAT (Lakehouse v2)
description: DATE_FORMAT — da formato a un valor de fecha o de fecha y hora según una cadena de formato.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-format.md
---

Da formato a un valor de fecha o de fecha y hora según una cadena de formato.

## Sintaxis de Analyze

```python
func.date_format(<date>, <format>)
```

## Ejemplos de Analyze

```python
func.date_format('2024-06-15', '%Y/%m/%d')

┌──────────────┐
│ '2024/06/15'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
DATE_FORMAT(<date>, <format>)
```

## Ejemplos de SQL

```sql
SELECT DATE_FORMAT('2024-06-15', '%Y/%m/%d');

┌────────────┐
│ 2024/06/15  │
└────────────┘
```
