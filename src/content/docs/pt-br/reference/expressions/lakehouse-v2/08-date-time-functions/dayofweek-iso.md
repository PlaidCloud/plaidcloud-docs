---
title: DAYOFWEEK_ISO (Lakehouse v2)
description: DAYOFWEEK_ISO — retorna o índice ISO do dia da semana de uma data (1=segunda-feira, 7=domingo).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofweek-iso.md
---

Retorna o índice ISO do dia da semana de uma data (1=segunda-feira, 7=domingo).

## Sintaxe do Analyze

```python
func.dayofweek_iso(<date>)
```

## Exemplos do Analyze

```python
func.dayofweek_iso('2024-06-15')

┌───┐
│ 6  │
└───┘
```

## Sintaxe SQL

```sql
DAYOFWEEK_ISO(<date>)
```

## Exemplos SQL

```sql
SELECT DAYOFWEEK_ISO('2024-06-15');

┌───┐
│ 6  │
└───┘
```
