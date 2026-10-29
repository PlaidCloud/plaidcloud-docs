---
title: NEXT_DAY (Lakehouse v2)
description: NEXT_DAY — devolve a data do próximo dia da semana especificado a seguir a uma data indicada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/next-day.md
---

Devolve a data do próximo dia da semana especificado a seguir a uma data indicada.

## Sintaxe de Analyze

```python
func.next_day(<date>, <weekday>)
```

## Exemplos de Analyze

```python
func.next_day('2024-06-15', 'Monday')

┌──────────────┐
│ '2024-06-17'  │
└──────────────┘
```

## Sintaxe SQL

```sql
NEXT_DAY(<date>, <weekday>)
```

## Exemplos SQL

```sql
SELECT NEXT_DAY('2024-06-15', 'Monday');

┌────────────┐
│ 2024-06-17  │
└────────────┘
```
