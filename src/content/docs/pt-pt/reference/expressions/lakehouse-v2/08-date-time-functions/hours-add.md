---
title: HOURS_ADD (Lakehouse v2)
description: HOURS_ADD — adiciona um número especificado de horas a uma data e hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hours-add.md
---

Adiciona um número especificado de horas a uma data e hora.

## Sintaxe do Analyze

```python
func.hours_add(<datetime>, <n>)
```

## Exemplos do Analyze

```python
func.hours_add('2024-01-01 10:00:00', 5)

┌───────────────────────┐
│ '2024-01-01 15:00:00'  │
└───────────────────────┘
```

## Sintaxe SQL

```sql
HOURS_ADD(<datetime>, <n>)
```

## Exemplos SQL

```sql
SELECT HOURS_ADD('2024-01-01 10:00:00', 5);

┌─────────────────────┐
│ 2024-01-01 15:00:00  │
└─────────────────────┘
```
