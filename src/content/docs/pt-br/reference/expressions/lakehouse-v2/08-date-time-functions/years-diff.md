---
title: YEARS_DIFF (Lakehouse v2)
description: YEARS_DIFF — retorna o número de anos entre duas datas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/years-diff.md
---

Retorna o número de anos entre duas datas.

## Sintaxe do Analyze

```python
func.years_diff(<end_date>, <start_date>)
```

## Exemplos do Analyze

```python
func.years_diff('2029-01-01', '2024-01-01')

┌───┐
│ 5  │
└───┘
```

## Sintaxe SQL

```sql
YEARS_DIFF(<end_date>, <start_date>)
```

## Exemplos de SQL

```sql
SELECT YEARS_DIFF('2029-01-01', '2024-01-01');

┌───┐
│ 5  │
└───┘
```
