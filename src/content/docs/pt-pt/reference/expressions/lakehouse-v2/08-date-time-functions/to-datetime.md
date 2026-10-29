---
title: TO_DATETIME (Lakehouse v2)
description: TO_DATETIME — converte um valor num datetime.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-datetime.md
---

Converte um valor num datetime.

## Sintaxe de Analyze

```python
func.to_datetime(<expr>)
```

## Exemplos de Analyze

```python
func.to_datetime('2024-06-15')

┌───────────────────────┐
│ '2024-06-15 00:00:00'  │
└───────────────────────┘
```

## Sintaxe SQL

```sql
TO_DATETIME(<expr>)
```

## Exemplos SQL

```sql
SELECT TO_DATETIME('2024-06-15');

┌─────────────────────┐
│ 2024-06-15 00:00:00  │
└─────────────────────┘
```
