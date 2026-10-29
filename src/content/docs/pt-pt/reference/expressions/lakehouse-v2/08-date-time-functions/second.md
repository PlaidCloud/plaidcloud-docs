---
title: SECOND (Lakehouse v2)
description: SECOND — devolve o segundo de um datetime.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/second.md
---

Devolve o segundo de um datetime.

## Sintaxe de Analyze

```python
func.second(<datetime>)
```

## Exemplos de Analyze

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

## Exemplos SQL

```sql
SELECT SECOND('2024-06-15 14:30:45');

┌────┐
│ 45  │
└────┘
```
