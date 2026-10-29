---
title: MONTHNAME (Lakehouse v2)
description: MONTHNAME — retorna o nome do mês de uma data.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/monthname.md
---

Retorna o nome do mês de uma data.

## Sintaxe do Analyze

```python
func.monthname(<date>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT MONTHNAME('2024-06-15');

┌──────┐
│ June  │
└──────┘
```
