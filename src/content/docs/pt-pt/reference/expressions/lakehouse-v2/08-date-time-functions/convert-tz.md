---
title: CONVERT_TZ (Lakehouse v2)
description: CONVERT_TZ — converte uma data e hora de um fuso horário para outro.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/convert-tz.md
---

Converte uma data e hora de um fuso horário para outro.

## Sintaxe do Analyze

```python
func.convert_tz(<datetime>, <from_tz>, <to_tz>)
```

## Exemplos do Analyze

```python
func.convert_tz('2024-01-01 12:00:00', 'UTC', 'America/New_York')

┌───────────────────────┐
│ '2024-01-01 07:00:00'  │
└───────────────────────┘
```

## Sintaxe SQL

```sql
CONVERT_TZ(<datetime>, <from_tz>, <to_tz>)
```

## Exemplos SQL

```sql
SELECT CONVERT_TZ('2024-01-01 12:00:00', 'UTC', 'America/New_York');

┌─────────────────────┐
│ 2024-01-01 07:00:00  │
└─────────────────────┘
```
