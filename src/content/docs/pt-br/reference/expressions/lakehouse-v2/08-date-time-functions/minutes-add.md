---
title: MINUTES_ADD (Lakehouse v2)
description: MINUTES_ADD — adiciona um número especificado de minutos a uma data e hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-add.md
---

Adiciona um número especificado de minutos a uma data e hora.

## Sintaxe do Analyze

```python
func.minutes_add(<datetime>, <n>)
```

## Exemplos do Analyze

```python
func.minutes_add('2024-01-01 10:00:00', 45)

┌───────────────────────┐
│ '2024-01-01 10:45:00'  │
└───────────────────────┘
```

## Sintaxe SQL

```sql
MINUTES_ADD(<datetime>, <n>)
```

## Exemplos de SQL

```sql
SELECT MINUTES_ADD('2024-01-01 10:00:00', 45);

┌─────────────────────┐
│ 2024-01-01 10:45:00  │
└─────────────────────┘
```
