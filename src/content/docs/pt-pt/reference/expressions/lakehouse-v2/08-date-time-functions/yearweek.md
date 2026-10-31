---
title: YEARWEEK (Lakehouse v2)
description: YEARWEEK — devolve o ano e o número da semana de uma data como um número inteiro.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/yearweek.md
---

Devolve o ano e o número da semana de uma data como um número inteiro.

## Sintaxe de Analyze

```python
func.yearweek(<date>[, <mode>])
```

## Exemplos de Analyze

```python
func.yearweek('2024-06-15')

┌────────┐
│ 202424  │
└────────┘
```

## Sintaxe SQL

```sql
YEARWEEK(<date>[, <mode>])
```

## Exemplos SQL

```sql
SELECT YEARWEEK('2024-06-15');

┌────────┐
│ 202424  │
└────────┘
```
