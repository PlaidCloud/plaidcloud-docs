---
title: DATE_ADD (Lakehouse v2)
description: DATE_ADD — adiciona um intervalo de tempo especificado a uma data ou datetime.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-add.md
---

Adiciona um intervalo de tempo especificado a uma data ou datetime.

## Sintaxe do Analyze

```python
func.date_add(<date>, INTERVAL <n> <unit>)
```

## Exemplos do Analyze

```python
func.date_add('2024-01-01', text('INTERVAL 30 DAY'))

┌──────────────┐
│ '2024-01-31'  │
└──────────────┘
```

## Sintaxe SQL

```sql
DATE_ADD(<date>, INTERVAL <n> <unit>)
```

## Exemplos SQL

```sql
SELECT DATE_ADD('2024-01-01', INTERVAL 30 DAY);

┌────────────┐
│ 2024-01-31  │
└────────────┘
```
