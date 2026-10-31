---
title: SECONDS_SUB (Lakehouse v2)
description: SECONDS_SUB — soustrait un nombre donné de secondes d'une date-heure.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-sub.md
---

Soustrait un nombre donné de secondes d'une date-heure.

## Syntaxe Analyze

```python
func.seconds_sub(<datetime>, <n>)
```

## Exemples Analyze

```python
func.seconds_sub('2024-01-01 00:01:30', 90)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## Syntaxe SQL

```sql
SECONDS_SUB(<datetime>, <n>)
```

## Exemples SQL

```sql
SELECT SECONDS_SUB('2024-01-01 00:01:30', 90);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```
