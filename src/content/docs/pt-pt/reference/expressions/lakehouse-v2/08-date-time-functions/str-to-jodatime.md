---
title: STR_TO_JODATIME (Lakehouse v2)
description: STR_TO_JODATIME — converte uma cadeia de caracteres num datetime através de padrões de formato Joda-Time.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str-to-jodatime.md
---

Converte uma cadeia de caracteres num datetime através de padrões de formato Joda-Time.

## Sintaxe de Analyze

```python
func.str_to_jodatime(<str>, <pattern>)
```

## Exemplos de Analyze

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

## Exemplos SQL

```sql
SELECT STR_TO_JODATIME('2024/06/15', 'yyyy/MM/dd');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
