---
title: YEARS_ADD (Lakehouse v2)
description: YEARS_ADD — adiciona um número especificado de anos a uma data.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/years-add.md
---

Adiciona um número especificado de anos a uma data.

## Sintaxe de Analyze

```python
func.years_add(<date>, <n>)
```

## Exemplos de Analyze

```python
func.years_add('2024-01-01', 5)

┌──────────────┐
│ '2029-01-01'  │
└──────────────┘
```

## Sintaxe SQL

```sql
YEARS_ADD(<date>, <n>)
```

## Exemplos SQL

```sql
SELECT YEARS_ADD('2024-01-01', 5);

┌────────────┐
│ 2029-01-01  │
└────────────┘
```
