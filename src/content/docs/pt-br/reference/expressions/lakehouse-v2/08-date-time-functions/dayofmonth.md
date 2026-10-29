---
title: DAYOFMONTH (Lakehouse v2)
description: DAYOFMONTH — retorna o dia do mês de uma data. Alias de `DAY`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofmonth.md
---

Retorna o dia do mês de uma data. Alias de `DAY`.

## Sintaxe do Analyze

```python
func.dayofmonth(<date>)
```

## Exemplos do Analyze

```python
func.dayofmonth('2024-06-15')

┌────┐
│ 15  │
└────┘
```

## Sintaxe SQL

```sql
DAYOFMONTH(<date>)
```

## Exemplos SQL

```sql
SELECT DAYOFMONTH('2024-06-15');

┌────┐
│ 15  │
└────┘
```
