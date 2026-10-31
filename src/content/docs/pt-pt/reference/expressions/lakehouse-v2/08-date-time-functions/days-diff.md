---
title: DAYS_DIFF (Lakehouse v2)
description: DAYS_DIFF — devolve o número de dias entre duas datas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/days-diff.md
---

Devolve o número de dias entre duas datas.

## Sintaxe do Analyze

```python
func.days_diff(<end_date>, <start_date>)
```

## Exemplos do Analyze

```python
func.days_diff('2024-03-01', '2024-01-01')

┌────┐
│ 60  │
└────┘
```

## Sintaxe SQL

```sql
DAYS_DIFF(<end_date>, <start_date>)
```

## Exemplos SQL

```sql
SELECT DAYS_DIFF('2024-03-01', '2024-01-01');

┌────┐
│ 60  │
└────┘
```
