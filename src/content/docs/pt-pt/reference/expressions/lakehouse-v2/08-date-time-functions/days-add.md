---
title: DAYS_ADD (Lakehouse v2)
description: DAYS_ADD — adiciona um número especificado de dias a uma data.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/days-add.md
---

Adiciona um número especificado de dias a uma data.

## Sintaxe do Analyze

```python
func.days_add(<date>, <n>)
```

## Exemplos do Analyze

```python
func.days_add('2024-01-01', 30)

┌──────────────┐
│ '2024-01-31'  │
└──────────────┘
```

## Sintaxe SQL

```sql
DAYS_ADD(<date>, <n>)
```

## Exemplos SQL

```sql
SELECT DAYS_ADD('2024-01-01', 30);

┌────────────┐
│ 2024-01-31  │
└────────────┘
```
