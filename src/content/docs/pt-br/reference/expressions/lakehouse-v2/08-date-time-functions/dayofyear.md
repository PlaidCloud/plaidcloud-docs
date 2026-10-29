---
title: DAYOFYEAR (Lakehouse v2)
description: DAYOFYEAR — retorna o dia do ano de uma data.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofyear.md
---

Retorna o dia do ano de uma data.

## Sintaxe do Analyze

```python
func.dayofyear(<date>)
```

## Exemplos do Analyze

```python
func.dayofyear('2024-06-15')

┌─────┐
│ 167  │
└─────┘
```

## Sintaxe SQL

```sql
DAYOFYEAR(<date>)
```

## Exemplos SQL

```sql
SELECT DAYOFYEAR('2024-06-15');

┌─────┐
│ 167  │
└─────┘
```
