---
title: MICROSECONDS_SUB (Lakehouse v2)
description: MICROSECONDS_SUB — subtrai um número especificado de microssegundos de uma data e hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/microseconds-sub.md
---

Subtrai um número especificado de microssegundos de uma data e hora.

## Sintaxe do Analyze

```python
func.microseconds_sub(<datetime>, <n>)
```

## Exemplos do Analyze

```python
func.microseconds_sub('2024-01-01 00:00:01', 1000000)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## Sintaxe SQL

```sql
MICROSECONDS_SUB(<datetime>, <n>)
```

## Exemplos de SQL

```sql
SELECT MICROSECONDS_SUB('2024-01-01 00:00:01', 1000000);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```
