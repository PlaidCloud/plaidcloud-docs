---
title: HOURS_DIFF (Lakehouse v2)
description: HOURS_DIFF — retorna o número de horas entre dois datetimes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hours-diff.md
---

Retorna o número de horas entre dois datetimes.

## Sintaxe do Analyze

```python
func.hours_diff(<end>, <start>)
```

## Exemplos do Analyze

```python
func.hours_diff('2024-01-02 10:00:00', '2024-01-01 10:00:00')

┌────┐
│ 24  │
└────┘
```

## Sintaxe SQL

```sql
HOURS_DIFF(<end>, <start>)
```

## Exemplos SQL

```sql
SELECT HOURS_DIFF('2024-01-02 10:00:00', '2024-01-01 10:00:00');

┌────┐
│ 24  │
└────┘
```
