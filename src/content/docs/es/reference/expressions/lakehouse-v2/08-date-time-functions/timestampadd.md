---
title: TIMESTAMPADD (Lakehouse v2)
description: TIMESTAMPADD — suma un intervalo de tiempo específico a un valor de fecha y hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestampadd.md
---

Suma un intervalo de tiempo específico a un valor de fecha y hora.

## Sintaxis de Analyze

```python
func.timestampadd(<unit>, <n>, <datetime>)
```

## Ejemplos de Analyze

```python
func.timestampadd('DAY', 7, '2024-01-01')

┌──────────────┐
│ '2024-01-08'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
TIMESTAMPADD(<unit>, <n>, <datetime>)
```

## Ejemplos de SQL

```sql
SELECT TIMESTAMPADD(DAY, 7, '2024-01-01');

┌────────────┐
│ 2024-01-08  │
└────────────┘
```
