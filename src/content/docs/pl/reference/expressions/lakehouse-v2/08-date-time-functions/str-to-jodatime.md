---
title: STR_TO_JODATIME (Lakehouse v2)
description: STR_TO_JODATIME — analizuje ciąg znaków do daty i godziny przy użyciu wzorców formatu Joda-Time.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str-to-jodatime.md
---

Analizuje ciąg znaków do daty i godziny przy użyciu wzorców formatu Joda-Time.

## Składnia Analyze

```python
func.str_to_jodatime(<str>, <pattern>)
```

## Przykłady Analyze

```python
func.str_to_jodatime('2024/06/15', 'yyyy/MM/dd')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Składnia SQL

```sql
STR_TO_JODATIME(<str>, <pattern>)
```

## Przykłady SQL

```sql
SELECT STR_TO_JODATIME('2024/06/15', 'yyyy/MM/dd');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
