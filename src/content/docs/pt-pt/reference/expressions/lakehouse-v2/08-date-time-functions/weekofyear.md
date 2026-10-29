---
title: WEEKOFYEAR (Lakehouse v2)
description: WEEKOFYEAR — devolve a semana do ano para uma data. Alias de `WEEK`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weekofyear.md
---

Devolve a semana do ano para uma data. Alias de `WEEK`.

## Sintaxe de Analyze

```python
func.weekofyear(<date>)
```

## Exemplos de Analyze

```python
func.weekofyear('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## Sintaxe SQL

```sql
WEEKOFYEAR(<date>)
```

## Exemplos SQL

```sql
SELECT WEEKOFYEAR('2024-06-15');

┌────┐
│ 24  │
└────┘
```
