---
title: TIME_FORMAT (Lakehouse v2)
description: TIME_FORMAT — formata um valor de hora de acordo com uma string de formato.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/time-format.md
---

Formata um valor de hora de acordo com uma string de formato.

## Sintaxe do Analyze

```python
func.time_format(<time>, <format>)
```

## Exemplos do Analyze

```python
func.time_format('14:30:00', '%H hours %i minutes')

┌───────────────────────┐
│ '14 hours 30 minutes'  │
└───────────────────────┘
```

## Sintaxe SQL

```sql
TIME_FORMAT(<time>, <format>)
```

## Exemplos de SQL

```sql
SELECT TIME_FORMAT('14:30:00', '%H hours %i minutes');

┌─────────────────────┐
│ 14 hours 30 minutes  │
└─────────────────────┘
```
