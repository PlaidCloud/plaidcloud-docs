---
title: QUARTER (Lakehouse v2)
description: QUARTER — retorna o trimestre do ano de uma data (1-4).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/quarter.md
---

Retorna o trimestre do ano de uma data (1-4).

## Sintaxe do Analyze

```python
func.quarter(<date>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT QUARTER('2024-06-15');

┌───┐
│ 2  │
└───┘
```
