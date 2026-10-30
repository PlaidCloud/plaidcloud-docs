---
title: MICROSECONDS_ADD (Lakehouse v2)
description: MICROSECONDS_ADD — adiciona um número especificado de microssegundos a um datetime.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/microseconds-add.md
---

Adiciona um número especificado de microssegundos a um datetime.

## Sintaxe de Analyze

```python
func.microseconds_add(<datetime>, <n>)
```

## Exemplos de Analyze

```python
func.microseconds_add('2024-01-01 00:00:00', 1000000)

┌───────────────────────┐
│ '2024-01-01 00:00:01'  │
└───────────────────────┘
```

## Sintaxe SQL

```sql
MICROSECONDS_ADD(<datetime>, <n>)
```

## Exemplos SQL

```sql
SELECT MICROSECONDS_ADD('2024-01-01 00:00:00', 1000000);

┌─────────────────────┐
│ 2024-01-01 00:00:01  │
└─────────────────────┘
```
