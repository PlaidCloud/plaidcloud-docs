---
title: QUARTER (Lakehouse v2)
description: QUARTER — devolve o trimestre do ano de uma data (1-4).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/quarter.md
---

Devolve o trimestre do ano de uma data (1-4).

## Sintaxe de Analyze

```python
func.quarter(<date>)
```

## Exemplos de Analyze

```python
func.quarter('2024-06-15')

┌───┐
│ 2  │
└───┘
```

## Sintaxe SQL

```sql
QUARTER(<date>)
```

## Exemplos SQL

```sql
SELECT QUARTER('2024-06-15');

┌───┐
│ 2  │
└───┘
```
