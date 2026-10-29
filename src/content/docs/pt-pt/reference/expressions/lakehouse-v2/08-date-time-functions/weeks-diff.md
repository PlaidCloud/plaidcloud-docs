---
title: WEEKS_DIFF (Lakehouse v2)
description: WEEKS_DIFF — devolve o número de semanas entre duas datas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weeks-diff.md
---

Devolve o número de semanas entre duas datas.

## Sintaxe de Analyze

```python
func.weeks_diff(<end_date>, <start_date>)
```

## Exemplos de Analyze

```python
func.weeks_diff('2024-03-01', '2024-01-01')

┌───┐
│ 8  │
└───┘
```

## Sintaxe SQL

```sql
WEEKS_DIFF(<end_date>, <start_date>)
```

## Exemplos SQL

```sql
SELECT WEEKS_DIFF('2024-03-01', '2024-01-01');

┌───┐
│ 8  │
└───┘
```
