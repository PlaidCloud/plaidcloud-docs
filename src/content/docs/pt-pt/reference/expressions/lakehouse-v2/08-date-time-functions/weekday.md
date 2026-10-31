---
title: WEEKDAY (Lakehouse v2)
description: WEEKDAY — devolve o índice do dia da semana para uma data (0=segunda-feira, 6=domingo).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weekday.md
---

Devolve o índice do dia da semana para uma data (0=segunda-feira, 6=domingo).

## Sintaxe de Analyze

```python
func.weekday(<date>)
```

## Exemplos de Analyze

```python
func.weekday('2024-06-15')

┌───┐
│ 5  │
└───┘
```

## Sintaxe SQL

```sql
WEEKDAY(<date>)
```

## Exemplos SQL

```sql
SELECT WEEKDAY('2024-06-15');

┌───┐
│ 5  │
└───┘
```
