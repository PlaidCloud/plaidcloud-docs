---
title: MONTHS_ADD (Lakehouse v2)
description: MONTHS_ADD — adiciona um número especificado de meses a uma data.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/months-add.md
---

Adiciona um número especificado de meses a uma data.

## Sintaxe de Analyze

```python
func.months_add(<date>, <n>)
```

## Exemplos de Analyze

```python
func.months_add('2024-01-15', 3)

┌──────────────┐
│ '2024-04-15'  │
└──────────────┘
```

## Sintaxe SQL

```sql
MONTHS_ADD(<date>, <n>)
```

## Exemplos SQL

```sql
SELECT MONTHS_ADD('2024-01-15', 3);

┌────────────┐
│ 2024-04-15  │
└────────────┘
```
