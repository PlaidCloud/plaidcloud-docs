---
title: SEC_TO_TIME (Lakehouse v2)
description: SEC_TO_TIME — convierte segundos en un valor de hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/sec-to-time.md
---

Convierte segundos en un valor de hora.

## Sintaxis de Analyze

```python
func.sec_to_time(<seconds>)
```

## Ejemplos de Analyze

```python
func.sec_to_time(3661)

┌────────────┐
│ '01:01:01'  │
└────────────┘
```

## Sintaxis de SQL

```sql
SEC_TO_TIME(<seconds>)
```

## Ejemplos de SQL

```sql
SELECT SEC_TO_TIME(3661);

┌──────────┐
│ 01:01:01  │
└──────────┘
```
