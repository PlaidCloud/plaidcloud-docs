---
title: MINUTES_ADD (Lakehouse v2)
description: MINUTES_ADD — adiciona um número especificado de minutos a um datetime.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-add.md
---

Adiciona um número especificado de minutos a um datetime.

## Sintaxe de Analyze

```python
func.minutes_add(<datetime>, <n>)
```

## Exemplos de Analyze

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

## Exemplos SQL

```sql
SELECT MINUTES_ADD('2024-01-01 10:00:00', 45);

┌─────────────────────┐
│ 2024-01-01 10:45:00  │
└─────────────────────┘
```
