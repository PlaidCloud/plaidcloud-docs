---
title: MONTHNAME (Lakehouse v2)
description: MONTHNAME — devolve o nome do mês de uma data.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/monthname.md
---

Devolve o nome do mês de uma data.

## Sintaxe de Analyze

```python
func.monthname(<date>)
```

## Exemplos de Analyze

```python
func.monthname('2024-06-15')

┌────────┐
│ 'June'  │
└────────┘
```

## Sintaxe SQL

```sql
MONTHNAME(<date>)
```

## Exemplos SQL

```sql
SELECT MONTHNAME('2024-06-15');

┌──────┐
│ June  │
└──────┘
```
