---
title: MINUTE (Lakehouse v2)
description: MINUTE — retorna o minuto de uma data e hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minute.md
---

Retorna o minuto de uma data e hora.

## Sintaxe do Analyze

```python
func.minute(<datetime>)
```

## Exemplos do Analyze

```python
func.minute('2024-06-15 14:30:00')

┌────┐
│ 30  │
└────┘
```

## Sintaxe SQL

```sql
MINUTE(<datetime>)
```

## Exemplos de SQL

```sql
SELECT MINUTE('2024-06-15 14:30:00');

┌────┐
│ 30  │
└────┘
```
