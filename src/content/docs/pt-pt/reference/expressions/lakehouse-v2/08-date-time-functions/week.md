---
title: WEEK (Lakehouse v2)
description: WEEK — devolve o número da semana do ano para uma data.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/week.md
---

Devolve o número da semana do ano para uma data.

## Sintaxe de Analyze

```python
func.week(<date>[, <mode>])
```

## Exemplos de Analyze

```python
func.week('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## Sintaxe SQL

```sql
WEEK(<date>[, <mode>])
```

## Exemplos SQL

```sql
SELECT WEEK('2024-06-15');

┌────┐
│ 24  │
└────┘
```
