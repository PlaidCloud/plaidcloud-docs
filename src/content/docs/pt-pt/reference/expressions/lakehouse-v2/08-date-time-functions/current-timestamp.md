---
title: CURRENT_TIMESTAMP (Lakehouse v2)
description: CURRENT_TIMESTAMP — devolve a data e hora atuais.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-timestamp.md
---

Devolve a data e hora atuais.

## Sintaxe do Analyze

```python
func.current_timestamp()
```

## Exemplos do Analyze

```python
func.current_timestamp()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## Sintaxe SQL

```sql
CURRENT_TIMESTAMP()
```

## Exemplos SQL

```sql
SELECT CURRENT_TIMESTAMP();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
