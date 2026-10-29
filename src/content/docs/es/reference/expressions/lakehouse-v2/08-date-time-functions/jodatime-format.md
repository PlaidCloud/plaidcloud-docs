---
title: JODATIME_FORMAT (Lakehouse v2)
description: JODATIME_FORMAT — da formato a una fecha o a un valor de fecha y hora mediante patrones de formato de Joda-Time.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/jodatime-format.md
---

Da formato a una fecha o a un valor de fecha y hora mediante patrones de formato de Joda-Time.

## Sintaxis de Analyze

```python
func.jodatime_format(<datetime>, <pattern>)
```

## Ejemplos de Analyze

```python
func.jodatime_format('2024-06-15', 'yyyy/MM/dd')

┌──────────────┐
│ '2024/06/15'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
JODATIME_FORMAT(<datetime>, <pattern>)
```

## Ejemplos de SQL

```sql
SELECT JODATIME_FORMAT('2024-06-15', 'yyyy/MM/dd');

┌────────────┐
│ 2024/06/15  │
└────────────┘
```
