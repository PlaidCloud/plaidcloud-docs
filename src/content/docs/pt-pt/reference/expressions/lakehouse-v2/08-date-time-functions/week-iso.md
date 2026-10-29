---
title: WEEK_ISO (Lakehouse v2)
description: WEEK_ISO — devolve o número da semana ISO do ano para uma data.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/week-iso.md
---

Devolve o número da semana ISO do ano para uma data.

## Sintaxe de Analyze

```python
func.week_iso(<date>)
```

## Exemplos de Analyze

```python
func.week_iso('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## Sintaxe SQL

```sql
WEEK_ISO(<date>)
```

## Exemplos SQL

```sql
SELECT WEEK_ISO('2024-06-15');

┌────┐
│ 24  │
└────┘
```
