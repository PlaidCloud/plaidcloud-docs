---
title: HOURS_SUB (Lakehouse v2)
description: HOURS_SUB — subtrai um número especificado de horas a uma data e hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hours-sub.md
---

Subtrai um número especificado de horas a uma data e hora.

## Sintaxe do Analyze

```python
func.hours_sub(<datetime>, <n>)
```

## Exemplos do Analyze

```python
func.hours_sub('2024-01-01 15:00:00', 5)

┌───────────────────────┐
│ '2024-01-01 10:00:00'  │
└───────────────────────┘
```

## Sintaxe SQL

```sql
HOURS_SUB(<datetime>, <n>)
```

## Exemplos SQL

```sql
SELECT HOURS_SUB('2024-01-01 15:00:00', 5);

┌─────────────────────┐
│ 2024-01-01 10:00:00  │
└─────────────────────┘
```
