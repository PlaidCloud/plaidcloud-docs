---
title: SECONDS_ADD (Lakehouse v2)
description: SECONDS_ADD — adiciona um número especificado de segundos a uma data e hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-add.md
---

Adiciona um número especificado de segundos a uma data e hora.

## Sintaxe do Analyze

```python
func.seconds_add(<datetime>, <n>)
```

## Exemplos do Analyze

```python
func.seconds_add('2024-01-01 00:00:00', 90)

┌───────────────────────┐
│ '2024-01-01 00:01:30'  │
└───────────────────────┘
```

## Sintaxe SQL

```sql
SECONDS_ADD(<datetime>, <n>)
```

## Exemplos de SQL

```sql
SELECT SECONDS_ADD('2024-01-01 00:00:00', 90);

┌─────────────────────┐
│ 2024-01-01 00:01:30  │
└─────────────────────┘
```
