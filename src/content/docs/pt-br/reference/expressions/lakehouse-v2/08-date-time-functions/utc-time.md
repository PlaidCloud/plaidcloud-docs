---
title: UTC_TIME (Lakehouse v2)
description: UTC_TIME — retorna a hora UTC atual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/utc-time.md
---

Retorna a hora UTC atual.

## Sintaxe do Analyze

```python
func.utc_time()
```

## Exemplos do Analyze

```python
func.utc_time()

┌────────────┐
│ '18:30:00'  │
└────────────┘
```

## Sintaxe SQL

```sql
UTC_TIME()
```

## Exemplos de SQL

```sql
SELECT UTC_TIME();

┌──────────┐
│ 18:30:00  │
└──────────┘
```
