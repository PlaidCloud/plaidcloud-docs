---
title: WEEKS_ADD (Lakehouse v2)
description: WEEKS_ADD — adiciona um número especificado de semanas a uma data.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weeks-add.md
---

Adiciona um número especificado de semanas a uma data.

## Sintaxe de Analyze

```python
func.weeks_add(<date>, <n>)
```

## Exemplos de Analyze

```python
func.weeks_add('2024-01-01', 2)

┌──────────────┐
│ '2024-01-15'  │
└──────────────┘
```

## Sintaxe SQL

```sql
WEEKS_ADD(<date>, <n>)
```

## Exemplos SQL

```sql
SELECT WEEKS_ADD('2024-01-01', 2);

┌────────────┐
│ 2024-01-15  │
└────────────┘
```
