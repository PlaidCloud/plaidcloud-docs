---
title: ADDDATE (Lakehouse v2)
description: ADDDATE — adiciona um intervalo de tempo especificado a uma data. Alias de `DATE_ADD`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/adddate.md
---

Adiciona um intervalo de tempo especificado a uma data. Alias de `DATE_ADD`.

## Sintaxe do Analyze

```python
func.adddate(<date>, INTERVAL <n> <unit>)
```

## Exemplos do Analyze

```python
func.adddate('2024-01-01', text('INTERVAL 7 DAY'))

┌──────────────┐
│ '2024-01-08'  │
└──────────────┘
```

## Sintaxe SQL

```sql
ADDDATE(<date>, INTERVAL <n> <unit>)
```

## Exemplos SQL

```sql
SELECT ADDDATE('2024-01-01', INTERVAL 7 DAY);

┌────────────┐
│ 2024-01-08  │
└────────────┘
```
