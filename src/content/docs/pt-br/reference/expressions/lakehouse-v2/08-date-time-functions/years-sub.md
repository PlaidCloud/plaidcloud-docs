---
title: YEARS_SUB (Lakehouse v2)
description: YEARS_SUB — subtrai um número especificado de anos de uma data.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/years-sub.md
---

Subtrai um número especificado de anos de uma data.

## Sintaxe do Analyze

```python
func.years_sub(<date>, <n>)
```

## Exemplos do Analyze

```python
func.years_sub('2029-01-01', 5)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## Sintaxe SQL

```sql
YEARS_SUB(<date>, <n>)
```

## Exemplos de SQL

```sql
SELECT YEARS_SUB('2029-01-01', 5);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
