---
title: MINUTES_SUB (Lakehouse v2)
description: MINUTES_SUB — subtrai um número especificado de minutos a um datetime.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-sub.md
---

Subtrai um número especificado de minutos a um datetime.

## Sintaxe de Analyze

```python
func.minutes_sub(<datetime>, <n>)
```

## Exemplos de Analyze

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

## Exemplos SQL

```sql
SELECT MINUTES_SUB('2024-01-01 10:45:00', 45);

┌─────────────────────┐
│ 2024-01-01 10:00:00  │
└─────────────────────┘
```
