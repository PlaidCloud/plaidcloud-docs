---
title: SECOND (Lakehouse v2)
description: SECOND — retorna o segundo de uma data e hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/second.md
---

Retorna o segundo de uma data e hora.

## Sintaxe do Analyze

```python
func.second(<datetime>)
```

## Exemplos do Analyze

```python
func.second('2024-06-15 14:30:45')

┌────┐
│ 45  │
└────┘
```

## Sintaxe SQL

```sql
SECOND(<datetime>)
```

## Exemplos de SQL

```sql
SELECT SECOND('2024-06-15 14:30:45');

┌────┐
│ 45  │
└────┘
```
