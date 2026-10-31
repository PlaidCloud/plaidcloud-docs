---
title: PREVIOUS_DAY (Lakehouse v2)
description: PREVIOUS_DAY — retorna a data do dia da semana especificado imediatamente anterior a uma data informada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/previous-day.md
---

Retorna a data do dia da semana especificado imediatamente anterior a uma data informada.

## Sintaxe do Analyze

```python
func.previous_day(<date>, <weekday>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT PREVIOUS_DAY('2024-06-15', 'Monday');

┌────────────┐
│ 2024-06-10  │
└────────────┘
```
