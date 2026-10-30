---
title: SUBDATE (Lakehouse v2)
description: SUBDATE — subtrai um intervalo de tempo a uma data. Alias de `DATE_SUB`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/subdate.md
---

Subtrai um intervalo de tempo a uma data. Alias de `DATE_SUB`.

## Sintaxe de Analyze

```python
func.subdate(<date>, INTERVAL <n> <unit>)
```

## Exemplos de Analyze

```python
func.subdate('2024-01-31', text('INTERVAL 7 DAY'))

┌──────────────┐
│ '2024-01-24'  │
└──────────────┘
```

## Sintaxe SQL

```sql
SUBDATE(<date>, INTERVAL <n> <unit>)
```

## Exemplos SQL

```sql
SELECT SUBDATE('2024-01-31', INTERVAL 7 DAY);

┌────────────┐
│ 2024-01-24  │
└────────────┘
```
