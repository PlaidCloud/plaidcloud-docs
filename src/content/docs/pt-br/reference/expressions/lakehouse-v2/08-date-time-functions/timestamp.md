---
title: TIMESTAMP (Lakehouse v2)
description: TIMESTAMP — converte uma data ou string em uma data e hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestamp.md
---

Converte uma data ou string em uma data e hora.

## Sintaxe do Analyze

```python
func.timestamp(<expr>)
```

## Exemplos do Analyze

```python
func.timestamp('2024-06-15')

┌───────────────────────┐
│ '2024-06-15 00:00:00'  │
└───────────────────────┘
```

## Sintaxe SQL

```sql
TIMESTAMP(<expr>)
```

## Exemplos de SQL

```sql
SELECT TIMESTAMP('2024-06-15');

┌─────────────────────┐
│ 2024-06-15 00:00:00  │
└─────────────────────┘
```
