---
title: PREVIOUS_DAY (Lakehouse v2)
description: PREVIOUS_DAY — devolve a data do dia da semana especificado anterior a uma data indicada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/previous-day.md
---

Devolve a data do dia da semana especificado anterior a uma data indicada.

## Sintaxe de Analyze

```python
func.previous_day(<date>, <weekday>)
```

## Exemplos de Analyze

```python
func.previous_day('2024-06-15', 'Monday')

┌──────────────┐
│ '2024-06-10'  │
└──────────────┘
```

## Sintaxe SQL

```sql
PREVIOUS_DAY(<date>, <weekday>)
```

## Exemplos SQL

```sql
SELECT PREVIOUS_DAY('2024-06-15', 'Monday');

┌────────────┐
│ 2024-06-10  │
└────────────┘
```
