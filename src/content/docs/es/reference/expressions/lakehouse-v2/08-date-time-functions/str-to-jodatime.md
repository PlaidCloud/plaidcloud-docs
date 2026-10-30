---
title: STR_TO_JODATIME (Lakehouse v2)
description: STR_TO_JODATIME — convierte una cadena en un valor de fecha y hora mediante patrones de formato de Joda-Time.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str-to-jodatime.md
---

Convierte una cadena en un valor de fecha y hora mediante patrones de formato de Joda-Time.

## Sintaxis de Analyze

```python
func.str_to_jodatime(<str>, <pattern>)
```

## Ejemplos de Analyze

```python
func.str_to_jodatime('2024/06/15', 'yyyy/MM/dd')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
STR_TO_JODATIME(<str>, <pattern>)
```

## Ejemplos de SQL

```sql
SELECT STR_TO_JODATIME('2024/06/15', 'yyyy/MM/dd');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
