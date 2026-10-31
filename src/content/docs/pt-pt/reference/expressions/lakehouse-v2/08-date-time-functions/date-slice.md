---
title: DATE_SLICE (Lakehouse v2)
description: "Utilize a função de data/hora DATE_SLICE no PlaidCloud Lakehouse. Converte uma determinada hora para o início ou o fim de um intervalo de tempo com base no período especificado."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-slice.md
---

Converte uma determinada hora para o início ou o fim de um intervalo de tempo com base no período especificado.

## Sintaxe do Analyze

```python
func.date_slice(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## Exemplos do Analyze

```python
func.date_slice('2024-06-15 14:35:00', text('INTERVAL 1 HOUR'))

┌───────────────────────┐
│ '2024-06-15 14:00:00'  │
└───────────────────────┘
```

## Sintaxe SQL

```sql
DATE_SLICE(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## Exemplos SQL

```sql
SELECT DATE_SLICE('2024-06-15 14:35:00', INTERVAL 1 HOUR);

┌─────────────────────┐
│ 2024-06-15 14:00:00  │
└─────────────────────┘
```
