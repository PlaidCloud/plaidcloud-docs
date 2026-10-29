---
title: YEARWEEK (Lakehouse v2)
description: YEARWEEK — retorna o ano e o número da semana de uma data como um inteiro.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/yearweek.md
---

Retorna o ano e o número da semana de uma data como um inteiro.

## Sintaxe do Analyze

```python
func.yearweek(<date>[, <mode>])
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT YEARWEEK('2024-06-15');

┌────────┐
│ 202424  │
└────────┘
```
