---
title: TIMESTAMPADD (Lakehouse v2)
description: TIMESTAMPADD — adiciona um intervalo de tempo especificado a um datetime.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestampadd.md
---

Adiciona um intervalo de tempo especificado a um datetime.

## Sintaxe de Analyze

```python
func.timestampadd(<unit>, <n>, <datetime>)
```

## Exemplos de Analyze

```python
func.timestampadd('DAY', 7, '2024-01-01')

┌──────────────┐
│ '2024-01-08'  │
└──────────────┘
```

## Sintaxe SQL

```sql
TIMESTAMPADD(<unit>, <n>, <datetime>)
```

## Exemplos SQL

```sql
SELECT TIMESTAMPADD(DAY, 7, '2024-01-01');

┌────────────┐
│ 2024-01-08  │
└────────────┘
```
