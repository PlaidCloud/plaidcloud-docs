---
title: MINUTES_SUB (Lakehouse v2)
description: MINUTES_SUB — subtrai um número especificado de minutos de uma data e hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-sub.md
---

Subtrai um número especificado de minutos de uma data e hora.

## Sintaxe do Analyze

```python
func.minutes_sub(<datetime>, <n>)
```

## Exemplos do Analyze

```python
func.minutes_sub('2024-01-01 10:45:00', 45)

┌───────────────────────┐
│ '2024-01-01 10:00:00'  │
└───────────────────────┘
```

## Sintaxe SQL

```sql
MINUTES_SUB(<datetime>, <n>)
```

## Exemplos de SQL

```sql
SELECT MINUTES_SUB('2024-01-01 10:45:00', 45);

┌─────────────────────┐
│ 2024-01-01 10:00:00  │
└─────────────────────┘
```
