---
title: WEEKS_SUB (Lakehouse v2)
description: WEEKS_SUB — subtrai um número especificado de semanas de uma data.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weeks-sub.md
---

Subtrai um número especificado de semanas de uma data.

## Sintaxe do Analyze

```python
func.weeks_sub(<date>, <n>)
```

## Exemplos do Analyze

```python
func.weeks_sub('2024-01-15', 2)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## Sintaxe SQL

```sql
WEEKS_SUB(<date>, <n>)
```

## Exemplos de SQL

```sql
SELECT WEEKS_SUB('2024-01-15', 2);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
