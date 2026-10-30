---
title: MINUTE (Lakehouse v2)
description: MINUTE — devolve o minuto de um datetime.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minute.md
---

Devolve o minuto de um datetime.

## Sintaxe de Analyze

```python
func.minute(<datetime>)
```

## Exemplos de Analyze

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

## Exemplos SQL

```sql
SELECT MINUTE('2024-06-15 14:30:00');

┌────┐
│ 30  │
└────┘
```
