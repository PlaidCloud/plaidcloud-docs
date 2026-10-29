---
title: JODATIME_FORMAT (Lakehouse v2)
description: JODATIME_FORMAT — formata uma data ou data e hora através de padrões de formato Joda-Time.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/jodatime-format.md
---

Formata uma data ou data e hora através de padrões de formato Joda-Time.

## Sintaxe do Analyze

```python
func.jodatime_format(<datetime>, <pattern>)
```

## Exemplos do Analyze

```python
func.jodatime_format('2024-06-15', 'yyyy/MM/dd')

┌──────────────┐
│ '2024/06/15'  │
└──────────────┘
```

## Sintaxe SQL

```sql
JODATIME_FORMAT(<datetime>, <pattern>)
```

## Exemplos SQL

```sql
SELECT JODATIME_FORMAT('2024-06-15', 'yyyy/MM/dd');

┌────────────┐
│ 2024/06/15  │
└────────────┘
```
