---
title: LAST_DAY (Lakehouse v2)
description: LAST_DAY — devolve o último dia do mês de uma determinada data.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/last-day.md
---

Devolve o último dia do mês de uma determinada data.

## Sintaxe do Analyze

```python
func.last_day(<date>[, <unit>])
```

## Exemplos do Analyze

```python
func.last_day('2024-02-15')

┌──────────────┐
│ '2024-02-29'  │
└──────────────┘
```

## Sintaxe SQL

```sql
LAST_DAY(<date>[, <unit>])
```

## Exemplos SQL

```sql
SELECT LAST_DAY('2024-02-15');

┌────────────┐
│ 2024-02-29  │
└────────────┘
```
