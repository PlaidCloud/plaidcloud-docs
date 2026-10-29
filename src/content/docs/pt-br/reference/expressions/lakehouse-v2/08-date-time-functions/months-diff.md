---
title: MONTHS_DIFF (Lakehouse v2)
description: MONTHS_DIFF — retorna o número de meses entre duas datas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/months-diff.md
---

Retorna o número de meses entre duas datas.

## Sintaxe do Analyze

```python
func.months_diff(<end_date>, <start_date>)
```

## Exemplos do Analyze

```python
func.months_diff('2024-06-01', '2024-01-01')

┌───┐
│ 5  │
└───┘
```

## Sintaxe SQL

```sql
MONTHS_DIFF(<end_date>, <start_date>)
```

## Exemplos de SQL

```sql
SELECT MONTHS_DIFF('2024-06-01', '2024-01-01');

┌───┐
│ 5  │
└───┘
```
