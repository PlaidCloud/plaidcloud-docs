---
title: FROM_DAYS (Lakehouse v2)
description: FROM_DAYS — converte uma contagem de dias numa data.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/from-days.md
---

Converte uma contagem de dias numa data.

## Sintaxe do Analyze

```python
func.from_days(<n>)
```

## Exemplos do Analyze

```python
func.from_days(738886)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## Sintaxe SQL

```sql
FROM_DAYS(<n>)
```

## Exemplos SQL

```sql
SELECT FROM_DAYS(738886);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
