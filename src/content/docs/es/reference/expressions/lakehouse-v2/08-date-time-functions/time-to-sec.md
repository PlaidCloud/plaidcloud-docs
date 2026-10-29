---
title: TIME_TO_SEC (Lakehouse v2)
description: TIME_TO_SEC — convierte un valor de hora en segundos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/time-to-sec.md
---

Convierte un valor de hora en segundos.

## Sintaxis de Analyze

```python
func.time_to_sec(<time>)
```

## Ejemplos de Analyze

```python
func.time_to_sec('01:01:01')

┌──────┐
│ 3661  │
└──────┘
```

## Sintaxis de SQL

```sql
TIME_TO_SEC(<time>)
```

## Ejemplos de SQL

```sql
SELECT TIME_TO_SEC('01:01:01');

┌──────┐
│ 3661  │
└──────┘
```
