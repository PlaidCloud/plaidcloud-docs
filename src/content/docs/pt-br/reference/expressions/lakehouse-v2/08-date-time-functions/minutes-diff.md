---
title: MINUTES_DIFF (Lakehouse v2)
description: MINUTES_DIFF — retorna o número de minutos entre duas datas e horas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-diff.md
---

Retorna o número de minutos entre duas datas e horas.

## Sintaxe do Analyze

```python
func.minutes_diff(<end>, <start>)
```

## Exemplos do Analyze

```python
func.minutes_diff('2024-01-01 11:00:00', '2024-01-01 10:00:00')

┌────┐
│ 60  │
└────┘
```

## Sintaxe SQL

```sql
MINUTES_DIFF(<end>, <start>)
```

## Exemplos de SQL

```sql
SELECT MINUTES_DIFF('2024-01-01 11:00:00', '2024-01-01 10:00:00');

┌────┐
│ 60  │
└────┘
```
