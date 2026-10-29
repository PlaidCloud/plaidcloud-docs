---
title: UTC_TIMESTAMP (Lakehouse v2)
description: UTC_TIMESTAMP — retorna a data e a hora UTC atuais.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/utc-timestamp.md
---

Retorna a data e a hora UTC atuais.

## Sintaxe do Analyze

```python
func.utc_timestamp()
```

## Exemplos do Analyze

```python
func.utc_timestamp()

┌───────────────────────┐
│ '2024-06-15 18:30:00'  │
└───────────────────────┘
```

## Sintaxe SQL

```sql
UTC_TIMESTAMP()
```

## Exemplos de SQL

```sql
SELECT UTC_TIMESTAMP();

┌─────────────────────┐
│ 2024-06-15 18:30:00  │
└─────────────────────┘
```
