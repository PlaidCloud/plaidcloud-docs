---
title: NEXT_DAY (Lakehouse v2)
description: NEXT_DAY — retorna a data do próximo dia da semana especificado após uma data informada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/next-day.md
---

Retorna a data do próximo dia da semana especificado após uma data informada.

## Sintaxe do Analyze

```python
func.next_day(<date>, <weekday>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT NEXT_DAY('2024-06-15', 'Monday');

┌────────────┐
│ 2024-06-17  │
└────────────┘
```
