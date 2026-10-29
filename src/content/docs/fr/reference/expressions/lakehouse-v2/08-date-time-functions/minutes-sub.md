---
title: MINUTES_SUB (Lakehouse v2)
description: MINUTES_SUB — soustrait un nombre donné de minutes d'une date-heure.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-sub.md
---

Soustrait un nombre donné de minutes d'une date-heure.

## Syntaxe Analyze

```python
func.minutes_sub(<datetime>, <n>)
```

## Exemples Analyze

```python
func.minutes_sub('2024-01-01 10:45:00', 45)

┌───────────────────────┐
│ '2024-01-01 10:00:00'  │
└───────────────────────┘
```

## Syntaxe SQL

```sql
MINUTES_SUB(<datetime>, <n>)
```

## Exemples SQL

```sql
SELECT MINUTES_SUB('2024-01-01 10:45:00', 45);

┌─────────────────────┐
│ 2024-01-01 10:00:00  │
└─────────────────────┘
```
