---
title: TIME_SLICE (Lakehouse v2)
description: TIME_SLICE — converte uma hora informada para o início ou o fim de um intervalo de tempo.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/time-slice.md
---

Converte uma hora informada para o início ou o fim de um intervalo de tempo.

## Sintaxe do Analyze

```python
func.time_slice(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## Exemplos do Analyze

```python
func.time_slice('2024-06-15 14:35:00', text('INTERVAL 15 MINUTE'))

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## Sintaxe SQL

```sql
TIME_SLICE(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## Exemplos de SQL

```sql
SELECT TIME_SLICE('2024-06-15 14:35:00', INTERVAL 15 MINUTE);

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
