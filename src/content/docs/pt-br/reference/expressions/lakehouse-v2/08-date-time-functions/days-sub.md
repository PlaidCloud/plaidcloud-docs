---
title: DAYS_SUB (Lakehouse v2)
description: DAYS_SUB — subtrai um número especificado de dias de uma data.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/days-sub.md
---

Subtrai um número especificado de dias de uma data.

## Sintaxe do Analyze

```python
func.days_sub(<date>, <n>)
```

## Exemplos do Analyze

```python
func.days_sub('2024-01-31', 30)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## Sintaxe SQL

```sql
DAYS_SUB(<date>, <n>)
```

## Exemplos SQL

```sql
SELECT DAYS_SUB('2024-01-31', 30);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
