---
title: STR_TO_JODATIME (Lakehouse v2)
description: STR_TO_JODATIME — converte uma string em uma data e hora usando padrões de formato do Joda-Time.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str-to-jodatime.md
---

Converte uma string em uma data e hora usando padrões de formato do Joda-Time.

## Sintaxe do Analyze

```python
func.str_to_jodatime(<str>, <pattern>)
```

## Exemplos do Analyze

```python
func.str_to_jodatime('2024/06/15', 'yyyy/MM/dd')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Sintaxe SQL

```sql
STR_TO_JODATIME(<str>, <pattern>)
```

## Exemplos de SQL

```sql
SELECT STR_TO_JODATIME('2024/06/15', 'yyyy/MM/dd');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
