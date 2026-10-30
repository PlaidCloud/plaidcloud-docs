---
title: STR_TO_JODATIME (Lakehouse v2)
description: STR_TO_JODATIME – wandelt eine Zeichenfolge mithilfe von Joda-Time-Formatmustern in ein Datum mit Uhrzeit um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str-to-jodatime.md
---

Wandelt eine Zeichenfolge mithilfe von Joda-Time-Formatmustern in ein Datum mit Uhrzeit um.

## Analyze-Syntax

```python
func.str_to_jodatime(<str>, <pattern>)
```

## Analyze-Beispiele

```python
func.str_to_jodatime('2024/06/15', 'yyyy/MM/dd')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL-Syntax

```sql
STR_TO_JODATIME(<str>, <pattern>)
```

## SQL-Beispiele

```sql
SELECT STR_TO_JODATIME('2024/06/15', 'yyyy/MM/dd');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
