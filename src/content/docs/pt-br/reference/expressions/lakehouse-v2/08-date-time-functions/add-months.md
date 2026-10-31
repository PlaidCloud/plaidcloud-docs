---
title: ADD_MONTHS (Lakehouse v2)
description: ADD_MONTHS — adiciona um número especificado de meses a uma data.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/add-months.md
---

Adiciona um número especificado de meses a uma data.

## Sintaxe do Analyze

```python
func.add_months(<date>, <months>)
```

## Exemplos do Analyze

```python
func.add_months('2024-01-31', 1)

┌──────────────┐
│ '2024-02-29'  │
└──────────────┘
```

## Sintaxe SQL

```sql
ADD_MONTHS(<date>, <months>)
```

## Exemplos SQL

```sql
SELECT ADD_MONTHS('2024-01-31', 1);

┌────────────┐
│ 2024-02-29  │
└────────────┘
```
