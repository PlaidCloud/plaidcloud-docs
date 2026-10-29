---
title: SECONDS_SUB (Lakehouse v2)
description: SECONDS_SUB — subtrai um número especificado de segundos a um datetime.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-sub.md
---

Subtrai um número especificado de segundos a um datetime.

## Sintaxe de Analyze

```python
func.seconds_sub(<datetime>, <n>)
```

## Exemplos de Analyze

```python
func.seconds_sub('2024-01-01 00:01:30', 90)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## Sintaxe SQL

```sql
SECONDS_SUB(<datetime>, <n>)
```

## Exemplos SQL

```sql
SELECT SECONDS_SUB('2024-01-01 00:01:30', 90);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```
