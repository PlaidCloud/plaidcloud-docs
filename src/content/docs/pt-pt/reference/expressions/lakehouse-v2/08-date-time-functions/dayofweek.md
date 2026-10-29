---
title: DAYOFWEEK (Lakehouse v2)
description: DAYOFWEEK — devolve o índice do dia da semana de uma data (1=domingo, 7=sábado).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofweek.md
---

Devolve o índice do dia da semana de uma data (1=domingo, 7=sábado).

## Sintaxe do Analyze

```python
func.dayofweek(<date>)
```

## Exemplos do Analyze

```python
func.dayofweek('2024-06-15')

┌───┐
│ 7  │
└───┘
```

## Sintaxe SQL

```sql
DAYOFWEEK(<date>)
```

## Exemplos SQL

```sql
SELECT DAYOFWEEK('2024-06-15');

┌───┐
│ 7  │
└───┘
```
