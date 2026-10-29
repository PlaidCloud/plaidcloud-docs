---
title: DAY (Lakehouse v2)
description: DAY — retorna o dia do mês de uma data.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/day.md
---

Retorna o dia do mês de uma data.

## Sintaxe do Analyze

```python
func.day(<date>)
```

## Exemplos do Analyze

```python
func.day('2024-06-15')

┌────┐
│ 15  │
└────┘
```

## Sintaxe SQL

```sql
DAY(<date>)
```

## Exemplos SQL

```sql
SELECT DAY('2024-06-15');

┌────┐
│ 15  │
└────┘
```
