---
title: TIMESTAMPADD (Lakehouse v2)
description: TIMESTAMPADD — ajoute un intervalle de temps spécifié à une date-heure.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestampadd.md
---

Ajoute un intervalle de temps spécifié à une date-heure.

## Syntaxe Analyze

```python
func.timestampadd(<unit>, <n>, <datetime>)
```

## Exemples Analyze

```python
func.timestampadd('DAY', 7, '2024-01-01')

┌──────────────┐
│ '2024-01-08'  │
└──────────────┘
```

## Syntaxe SQL

```sql
TIMESTAMPADD(<unit>, <n>, <datetime>)
```

## Exemples SQL

```sql
SELECT TIMESTAMPADD(DAY, 7, '2024-01-01');

┌────────────┐
│ 2024-01-08  │
└────────────┘
```
