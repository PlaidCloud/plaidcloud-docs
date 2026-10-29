---
title: UTC_TIMESTAMP (Lakehouse v2)
description: UTC_TIMESTAMP — devolve a data e hora UTC atuais.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/utc-timestamp.md
---

Devolve a data e hora UTC atuais.

## Sintaxe de Analyze

```python
func.utc_timestamp()
```

## Exemplos de Analyze

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

## Exemplos SQL

```sql
SELECT UTC_TIMESTAMP();

┌─────────────────────┐
│ 2024-06-15 18:30:00  │
└─────────────────────┘
```
