---
title: SECONDS_DIFF (Lakehouse v2)
description: SECONDS_DIFF — retorna o número de segundos entre duas datas e horas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-diff.md
---

Retorna o número de segundos entre duas datas e horas.

## Sintaxe do Analyze

```python
func.seconds_diff(<end>, <start>)
```

## Exemplos do Analyze

```python
func.seconds_diff('2024-01-01 00:01:30', '2024-01-01 00:00:00')

┌────┐
│ 90  │
└────┘
```

## Sintaxe SQL

```sql
SECONDS_DIFF(<end>, <start>)
```

## Exemplos de SQL

```sql
SELECT SECONDS_DIFF('2024-01-01 00:01:30', '2024-01-01 00:00:00');

┌────┐
│ 90  │
└────┘
```
