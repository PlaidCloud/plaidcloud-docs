---
title: DATE_SUB (Lakehouse v2)
description: DATE_SUB — subtrai um intervalo de tempo especificado de uma data ou datetime.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-sub.md
---

Subtrai um intervalo de tempo especificado de uma data ou datetime.

## Sintaxe do Analyze

```python
func.date_sub(<date>, INTERVAL <n> <unit>)
```

## Exemplos do Analyze

```python
func.date_sub('2024-03-01', text('INTERVAL 1 MONTH'))

┌──────────────┐
│ '2024-02-01'  │
└──────────────┘
```

## Sintaxe SQL

```sql
DATE_SUB(<date>, INTERVAL <n> <unit>)
```

## Exemplos SQL

```sql
SELECT DATE_SUB('2024-03-01', INTERVAL 1 MONTH);

┌────────────┐
│ 2024-02-01  │
└────────────┘
```
