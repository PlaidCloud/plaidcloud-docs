---
title: JODATIME_FORMAT (Lakehouse v2)
description: JODATIME_FORMAT — formatuje datę lub datę i godzinę przy użyciu wzorców formatu Joda-Time.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/jodatime-format.md
---

Formatuje datę lub datę i godzinę przy użyciu wzorców formatu Joda-Time.

## Składnia Analyze

```python
func.jodatime_format(<datetime>, <pattern>)
```

## Przykłady Analyze

```python
func.jodatime_format('2024-06-15', 'yyyy/MM/dd')

┌──────────────┐
│ '2024/06/15'  │
└──────────────┘
```

## Składnia SQL

```sql
JODATIME_FORMAT(<datetime>, <pattern>)
```

## Przykłady SQL

```sql
SELECT JODATIME_FORMAT('2024-06-15', 'yyyy/MM/dd');

┌────────────┐
│ 2024/06/15  │
└────────────┘
```
