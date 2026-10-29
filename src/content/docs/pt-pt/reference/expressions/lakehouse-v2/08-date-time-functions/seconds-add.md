---
title: SECONDS_ADD (Lakehouse v2)
description: SECONDS_ADD — adiciona um número especificado de segundos a um datetime.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-add.md
---

Adiciona um número especificado de segundos a um datetime.

## Sintaxe de Analyze

```python
func.seconds_add(<datetime>, <n>)
```

## Exemplos de Analyze

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

## Exemplos SQL

```sql
SELECT SECONDS_ADD('2024-01-01 00:00:00', 90);

┌─────────────────────┐
│ 2024-01-01 00:01:30  │
└─────────────────────┘
```
