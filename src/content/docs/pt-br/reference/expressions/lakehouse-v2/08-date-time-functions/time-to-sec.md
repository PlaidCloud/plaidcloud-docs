---
title: TIME_TO_SEC (Lakehouse v2)
description: TIME_TO_SEC — converte um valor de hora em segundos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/time-to-sec.md
---

Converte um valor de hora em segundos.

## Sintaxe do Analyze

```python
func.time_to_sec(<time>)
```

## Exemplos do Analyze

```python
func.time_to_sec('01:01:01')

┌──────┐
│ 3661  │
└──────┘
```

## Sintaxe SQL

```sql
TIME_TO_SEC(<time>)
```

## Exemplos de SQL

```sql
SELECT TIME_TO_SEC('01:01:01');

┌──────┐
│ 3661  │
└──────┘
```
