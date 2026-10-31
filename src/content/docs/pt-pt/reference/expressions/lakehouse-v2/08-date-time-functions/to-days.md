---
title: TO_DAYS (Lakehouse v2)
description: TO_DAYS — converte uma data numa contagem de dias.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-days.md
---

Converte uma data numa contagem de dias.

## Sintaxe de Analyze

```python
func.to_days(<date>)
```

## Exemplos de Analyze

```python
func.to_days('2024-01-01')

┌────────┐
│ 738886  │
└────────┘
```

## Sintaxe SQL

```sql
TO_DAYS(<date>)
```

## Exemplos SQL

```sql
SELECT TO_DAYS('2024-01-01');

┌────────┐
│ 738886  │
└────────┘
```
