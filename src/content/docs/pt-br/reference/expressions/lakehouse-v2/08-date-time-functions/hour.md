---
title: HOUR (Lakehouse v2)
description: HOUR — retorna a hora de um datetime.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hour.md
---

Retorna a hora de um datetime.

## Sintaxe do Analyze

```python
func.hour(<datetime>)
```

## Exemplos do Analyze

```python
func.hour('2024-06-15 14:30:00')

┌────┐
│ 14  │
└────┘
```

## Sintaxe SQL

```sql
HOUR(<datetime>)
```

## Exemplos SQL

```sql
SELECT HOUR('2024-06-15 14:30:00');

┌────┐
│ 14  │
└────┘
```
