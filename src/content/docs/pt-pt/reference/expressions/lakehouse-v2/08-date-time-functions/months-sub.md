---
title: MONTHS_SUB (Lakehouse v2)
description: MONTHS_SUB — subtrai um número especificado de meses a uma data.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/months-sub.md
---

Subtrai um número especificado de meses a uma data.

## Sintaxe de Analyze

```python
func.months_sub(<date>, <n>)
```

## Exemplos de Analyze

```python
func.months_sub('2024-06-15', 3)

┌──────────────┐
│ '2024-03-15'  │
└──────────────┘
```

## Sintaxe SQL

```sql
MONTHS_SUB(<date>, <n>)
```

## Exemplos SQL

```sql
SELECT MONTHS_SUB('2024-06-15', 3);

┌────────────┐
│ 2024-03-15  │
└────────────┘
```
