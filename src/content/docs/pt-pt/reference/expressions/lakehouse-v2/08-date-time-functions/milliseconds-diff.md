---
title: MILLISECONDS_DIFF (Lakehouse v2)
description: MILLISECONDS_DIFF — devolve o número de milissegundos entre dois datetimes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/milliseconds-diff.md
---

Devolve o número de milissegundos entre dois datetimes.

## Sintaxe de Analyze

```python
func.milliseconds_diff(<end>, <start>)
```

## Exemplos de Analyze

```python
func.milliseconds_diff('2024-01-01 00:00:01', '2024-01-01 00:00:00')

┌──────┐
│ 1000  │
└──────┘
```

## Sintaxe SQL

```sql
MILLISECONDS_DIFF(<end>, <start>)
```

## Exemplos SQL

```sql
SELECT MILLISECONDS_DIFF('2024-01-01 00:00:01', '2024-01-01 00:00:00');

┌──────┐
│ 1000  │
└──────┘
```
