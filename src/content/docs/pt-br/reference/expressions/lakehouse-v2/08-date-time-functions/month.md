---
title: MONTH (Lakehouse v2)
description: MONTH — retorna o mês de uma data.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/month.md
---

Retorna o mês de uma data.

## Sintaxe do Analyze

```python
func.month(<date>)
```

## Exemplos do Analyze

```python
func.month('2024-06-15')

┌───┐
│ 6  │
└───┘
```

## Sintaxe SQL

```sql
MONTH(<date>)
```

## Exemplos de SQL

```sql
SELECT MONTH('2024-06-15');

┌───┐
│ 6  │
└───┘
```
