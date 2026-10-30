---
title: DAYS_SUB (Lakehouse v2)
description: DAYS_SUB — soustrait un nombre de jours donné d'une date.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/days-sub.md
---

Soustrait un nombre de jours donné d'une date.

## Syntaxe Analyze

```python
func.days_sub(<date>, <n>)
```

## Exemples Analyze

```python
func.days_sub('2024-01-31', 30)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## Syntaxe SQL

```sql
DAYS_SUB(<date>, <n>)
```

## Exemples SQL

```sql
SELECT DAYS_SUB('2024-01-31', 30);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
