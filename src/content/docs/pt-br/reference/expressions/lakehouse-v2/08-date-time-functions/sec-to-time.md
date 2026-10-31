---
title: SEC_TO_TIME (Lakehouse v2)
description: SEC_TO_TIME — converte segundos em um valor de hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/sec-to-time.md
---

Converte segundos em um valor de hora.

## Sintaxe do Analyze

```python
func.sec_to_time(<seconds>)
```

## Exemplos do Analyze

```python
func.sec_to_time(3661)

┌────────────┐
│ '01:01:01'  │
└────────────┘
```

## Sintaxe SQL

```sql
SEC_TO_TIME(<seconds>)
```

## Exemplos de SQL

```sql
SELECT SEC_TO_TIME(3661);

┌──────────┐
│ 01:01:01  │
└──────────┘
```
